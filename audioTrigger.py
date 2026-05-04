import pyaudio
from pydub import AudioSegment
import numpy as np
import wave
import time
from STT import STT
import os

class audioTrigger:

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    SOGLIA_SQUELCH = 500  # Regola questo valore in base al volume della radio
    SILENZIO_POST_TRASM = 2 # Secondi di silenzio prima di chiudere il file
    
    def __init__(self):
        # Stato Interno
        self.p = pyaudio.PyAudio()
        self.buffer = [] # Qui accumuliamo i chunk durante la trasmissione
        self.is_recording = False
        self.silence_start_time = None
        self.id_trasmissione = self._get_next_id() # ID iniziale
        
        self.stream = self.p.open(
            format=self.FORMAT, channels=self.CHANNELS,
            rate=self.RATE, input=True, frames_per_buffer=self.CHUNK
        )

    def setChunk(self, chunks):
        try:
            if chunks in [512, 1024, 2048, 4096]:
                self.CHUNK==chunks
                self._start_stream() # Necessario riavviare
        except:
            print("Usa una potenza di 2 standard (512, 1024, 2048)")        
    
    def setRate(self, rate):
        """Imposta il Sample Rate (8000, 16000, 44100, 48000)"""
        standard_rates = [8000, 16000, 32000, 44100, 48000]
        if rate in standard_rates:
            self.RATE = rate
            self._start_stream()
            print(f"Sample Rate impostato a {rate}Hz")
        else:
            print(f"Rate non standard. Scegli tra: {standard_rates}")
    
    def setSquelch(self, valore):
        """imposta la sensibilità del volume per far scattare la registrazione"""
        try:
            v = float(valore)
            if v >= 0:
                self.SOGLIA_SQUELCH = v
                print(f"Soglia Squelch impostata a {v}")
        except ValueError:
            print("Inserisci un numero non negativo per lo Squelch")

    def setSilenzioPostTrasm(self, secondi):
        """Imposta quanti secondi attendere prima di chiudere la registrazione"""
        try:
            s = float(secondi)
            if s > 0:
                self.SILENZIO_POST_TRASM = s
                print(f"Silenzio post-trasmissione: {s}s")
        except ValueError:
            print("Inserisci un numero di secondi non negativo")

    def stopRecord(self):
        print(f"[ID {self.id_trasmissione:03d}] Fine trasmissione.")
        self.salva_mp3()
        self.is_recording = False
        self.silence_start_time = None

    
    def getNextId(self):
        """Trova l'ultimo numero ID nella cartella e restituisce il successivo"""
        files = [f for f in os.listdir('.') if f.startswith("record_") and f.endswith(".mp3")]
        if not files:
            return 1
        # Estrae i numeri dai nomi file (es: record_005.mp3 -> 5)
        ids = [int(f.split('_')[1].split('.')[0]) for f in files]
        return max(ids) + 1

    def salvaMp3(self):
        """Converte il buffer in MP3 e lo salva con ID incrementale"""
        if not self.buffer:
            return

        # Trasforma i chunk audio in un oggetto AudioSegment
        raw_data = b''.join(self.buffer)
        audio_segment = AudioSegment(
            data=raw_data,
            sample_width=self.p.get_sample_size(self.FORMAT),
            frame_rate=self.RATE,
            channels=self.CHANNELS
        )

        # Nome file con padding (es: record_001.mp3)
        filename = f"record_{self.id_trasmissione:03d}.mp3"
        audio_segment.export(filename, format="mp3")
        
        print(f"--- Salvato: {filename} ---")
        
        # Incrementa l'ID per la prossima volta
        self.id_trasmissione += 1
        self.buffer = [] # Svuota il buffer

def ascolta(self):
        print(f"Radio in ascolto (ID Corrente: {self.id_trasmissione:03d})...")
        try:
            while True:
                data = self.stream.read(self.CHUNK, exception_on_overflow=False)
                audio_np = np.frombuffer(data, dtype=np.int16)
                rms = np.sqrt(np.mean(audio_np**2))

                if rms > self.SOGLIA_SQUELCH:
                    # C'è segnale!
                    if not self.is_recording:
                        print(f"\n[ID {self.id_trasmissione:03d}] Trasmissione iniziata...")
                        self.is_recording = True
                    
                    self.buffer.append(data)
                    self.silence_start_time = None # Resetta il timer del silenzio
                
                elif self.is_recording:
                    # Silenzio, ma stavamo registrando
                    if self.silence_start_time is None:
                        self.silence_start_time = time.time()
                    
                    self.buffer.append(data) # Registriamo anche un po' di silenzio finale

                    # Se il silenzio dura troppo, chiudiamo il file
                    if time.time() - self.silence_start_time > self.SILENZIO_POST_TRASM:
                        self.stopRecord()


        except KeyboardInterrupt:
            print("\nMonitoraggio interrotto.")
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
