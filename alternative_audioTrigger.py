import pyaudio
import numpy as np
import torch
import time
import os
from pydub import AudioSegment


class alternative_audioTrigger:

    CHUNK    = 512    # Silero VAD richiede esattamente 512 campioni a 16kHz
    FORMAT   = pyaudio.paInt16
    CHANNELS = 1
    RATE     = 16000  # Silero VAD richiede 16kHz

    VAD_THRESHOLD       = 0.5  # probabilità minima per considerare voce attiva (0.0 - 1.0)
    SILENZIO_POST_TRASM = 2    # secondi di silenzio prima di chiudere la registrazione

    def __init__(self, device_index: int = None):
        # Stato interno
        self.device_index      = device_index
        self.buffer            = []
        self.is_recording      = False
        self.silence_start     = None
        self.id_trasmissione   = self._get_next_id()
        self._running          = False

        # callback chiamata quando un file MP3 è pronto (collegare a RadioController)
        self.on_trasmissione_finita = None

        # PyAudio
        self.p      = pyaudio.PyAudio()
        self.stream = None

        # Silero VAD
        print("Caricamento Silero VAD...")
        self.vad_model, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-vad",
            model="silero_vad",
            force_reload=False
        )
        self.vad_model.eval()
        print("Silero VAD pronto.")

    #CONTROLLO STREAM#

    def _apri_stream(self):
        """Apre lo stream PyAudio con il device selezionato."""
        kwargs = dict(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )
        if self.device_index is not None:
            kwargs["input_device_index"] = self.device_index
        self.stream = self.p.open(**kwargs)

    def startListen(self):
        """Avvia il loop di ascolto."""
        self._running = True
        self._apri_stream()
        self._ascolta()

    def stopListen(self):
        """Ferma il loop di ascolto."""
        self._running = False

    #LOOP PRINCIPALE#

    def _ascolta(self):
        print(f"In ascolto (ID corrente: {self.id_trasmissione:03d})...")
        try:
            while self._running:
                data     = self.stream.read(self.CHUNK, exception_on_overflow=False)
                audio_np = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
                tensor   = torch.from_numpy(audio_np)

                # Silero VAD: probabilità che ci sia voce
                with torch.no_grad():
                    prob = self.vad_model(tensor, self.RATE).item()

                voce_rilevata = prob >= self.VAD_THRESHOLD

                if voce_rilevata:
                    if not self.is_recording:
                        print(f"\n[ID {self.id_trasmissione:03d}] Trasmissione iniziata (prob={prob:.2f})")
                        self.is_recording = True
                    self.buffer.append(data)
                    self.silence_start = None

                elif self.is_recording:
                    self.buffer.append(data)  # registra anche il silenzio finale
                    if self.silence_start is None:
                        self.silence_start = time.time()
                    if time.time() - self.silence_start > self.SILENZIO_POST_TRASM:
                        self._stopRecord()

        except Exception as e:
            print(f"Errore nel loop di ascolto: {e}")
        finally:
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()

    #FINE TRASMISSIONE#

    def _stopRecord(self):
        """Chiude la registrazione corrente e salva il file MP3."""
        print(f"[ID {self.id_trasmissione:03d}] Fine trasmissione.")
        filename = self._salva_mp3()
        self.is_recording  = False
        self.silence_start = None

        # Notifica il controller che il file è pronto
        if filename and self.on_trasmissione_finita:
            self.on_trasmissione_finita(filename)

    def _salva_mp3(self) -> str:
        """Salva il buffer come file MP3 e restituisce il path."""
        if not self.buffer:
            return ""

        raw_data      = b"".join(self.buffer)
        audio_segment = AudioSegment(
            data=raw_data,
            sample_width=self.p.get_sample_size(self.FORMAT),
            frame_rate=self.RATE,
            channels=self.CHANNELS
        )

        os.makedirs("recordings", exist_ok=True)
        filename = os.path.join("recordings", f"record_{self.id_trasmissione:03d}.mp3")
        audio_segment.export(filename, format="mp3")
        print(f"--- Salvato: {filename} ---")

        self.id_trasmissione += 1
        self.buffer = []
        return filename

    #IMPOSTAZIONI#

    def setVadThreshold(self, valore: float):
        """Soglia VAD (0.0 - 1.0). Più alto = meno sensibile."""
        if 0.0 <= valore <= 1.0:
            self.VAD_THRESHOLD = valore
        else:
            print("La soglia VAD deve essere tra 0.0 e 1.0")

    def setSilenzioPostTrasm(self, secondi: float):
        """Secondi di silenzio prima di chiudere la registrazione."""
        if secondi > 0:
            self.SILENZIO_POST_TRASM = secondi
        else:
            print("Inserisci un valore positivo")

    def setDeviceIndex(self, index: int):
        """Cambia il dispositivo audio. Riavvia lo stream se attivo."""
        self.device_index = index
        if self._running:
            self.stream.stop_stream()
            self.stream.close()
            self._apri_stream()

    #UTILITY#

    def _get_next_id(self) -> int:
        """Trova l'ID successivo guardando i file già salvati."""
        os.makedirs("recordings", exist_ok=True)
        files = [f for f in os.listdir("recordings") if f.startswith("record_") and f.endswith(".mp3")]
        if not files:
            return 1
        ids = [int(f.split("_")[1].split(".")[0]) for f in files]
        return max(ids) + 1

    def get_input_devices(self) -> list[dict]:
        """Restituisce la lista dei dispositivi di input disponibili."""
        devices = []
        for i in range(self.p.get_device_count()):
            info = self.p.get_device_info_by_index(i)
            if info["maxInputChannels"] > 0:
                devices.append({"index": i, "name": info["name"]})
        return devices

    def terminate(self):
        """Rilascia le risorse PyAudio."""
        self.stopListen()
        self.p.terminate()