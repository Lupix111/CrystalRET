import threading
import os
import shutil
from STT import STT
from audioTrigger import audioTrigger
from localOllama import LocalOllama
from alternative_audioTrigger import alternative_audioTrigger
from PySide6.QtCore import QThread, QObject, Signal
from utils import get_base_dir


class AudioWorker(QThread):
    def __init__(self, audio):
        super().__init__()
        self.audio = audio

    def run(self):
        self.audio.startListen()


class radioController(QObject):
    transcription_ready = Signal(str, float)
    ai_response_ready   = Signal(str)
    squelch_changed = Signal(bool)
    audio_level_changed = Signal(int)  # 0-100


    def __init__(self):
        super().__init__()

        base = get_base_dir()
        self.dir_recordings    = os.path.join(base, "recordings")
        self.dir_transcript    = os.path.join(base, "input_transcript")
        self.dir_processed     = os.path.join(base, "already_processed_transcript")
        self.log_path          = os.path.join(base, "log_radio.txt")

        os.makedirs(self.dir_recordings, exist_ok=True)
        os.makedirs(self.dir_transcript, exist_ok=True)
        os.makedirs(self.dir_processed,  exist_ok=True)

        self.stt   = STT()
        self.testo = ""
        self.ollama = LocalOllama()

        # trigger con Silero VAD
        self.audio = alternative_audioTrigger(recordings_dir=self.dir_recordings)
        self.audio_worker = AudioWorker(self.audio)
        self.audio.on_trasmissione_finita = self.gestisci_fine_trasmissione
        self.audio.on_trasmissione_iniziata = self._on_iniziata
        self.audio.on_rec_stop              = self._on_rec_stop
        self.audio.on_audio_level = self._on_audio_level
        

        # legacy — decommentare per tornare al trigger originale
        # self.audio = audioTrigger()
        # self.audio.on_trasmissione_finita = self.gestisci_fine_trasmissione

    def esegui_analisi(self, file_mp3):
        print(f"Analisi STT iniziata per {file_mp3}...")
        self.testo, durata = self.stt.startTranscibe(file_mp3)
        if not self.testo:
            return

        print(f"RISULTATO STT: {self.testo}")
        self.transcription_ready.emit(self.testo, durata)

        # salva transcript
        nome_base       = os.path.splitext(os.path.basename(file_mp3))[0]
        transcript_path = os.path.join(self.dir_transcript, f"{nome_base}.txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(self.testo)

        # analisi Ollama
        risultato = self.ollama.analisiFile(self.testo)
        self.ai_response_ready.emit(risultato)

        # sposta in already_processed
        shutil.move(transcript_path, os.path.join(self.dir_processed, f"{nome_base}.txt"))

        # log testuale
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"[{file_mp3}] {self.testo}\n")
        

    def _on_iniziata(self):
        self.squelch_changed.emit(True)

    def _on_rec_stop(self):
        self.squelch_changed.emit(False)

    def _on_audio_level(self, valore: int):
        self.audio_level_changed.emit(valore)

    def gestisci_fine_trasmissione(self, file_mp3):
        thread_stt = threading.Thread(target=self.esegui_analisi, args=(file_mp3,))
        thread_stt.start()

    # --- controlli Silero VAD ---
    def setVadThreshold(self, valore):
        self.audio.setVadThreshold(valore)

    def stopListenVad(self):
        self.audio.stopListen()
        if self.audio_worker.isRunning():
            self.audio_worker.wait(3000)

    def startListenVad(self):
        self.audio_worker = AudioWorker(self.audio)
        self.audio_worker.start()

    def setModelSTT(self, model_size: str, on_finished=None, on_error=None):
        class _Loader(QThread):
            finished = Signal()
            error    = Signal(str)

            def __init__(self, stt, size):
                super().__init__()
                self.stt  = stt
                self.size = size

            def run(self):
                try:
                    self.stt.setModel(self.size)
                    self.finished.emit()
                except Exception as e:
                    self.error.emit(str(e))

        self._model_loader = _Loader(self.stt, model_size)
        if on_finished:
            self._model_loader.finished.connect(on_finished)
        if on_error:
            self._model_loader.error.connect(on_error)
        self._model_loader.start()