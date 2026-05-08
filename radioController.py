import threading
from STT import STT
from audioTrigger import audioTrigger
from localOllama import LocalOllama
from alternative_audioTrigger import alternative_audioTrigger
from PySide6.QtCore import QThread
import os
import shutil


class AudioWorker(QThread):
    def __init__(self, audio):
        super().__init__()
        self.audio = audio

    def run(self):
        self.audio.startListen()

class radioController:
    def __init__(self):
        # Ci assicuriamo che le cartelle esistono, sennò le creiamo
        os.makedirs("recordings", exist_ok=True)
        os.makedirs("input_transcript", exist_ok=True)
        os.makedirs("already_processed_transcript", exist_ok=True)
        
        #self.alt_audio = audioTrigger() #vecchio audio trigger
        self.stt = STT()
        self.testo = ""
        self.ollama = LocalOllama()

        # trigger con Silero VAD
        self.audio = alternative_audioTrigger()
        self.audio_worker = AudioWorker(self.audio)
        self.audio.on_trasmissione_finita = self.gestisci_fine_trasmissione
        
        # legacy — istanziare solo se si vuole tornare al trigger originale
        # self.audio = audioTrigger()
        # self.audio.on_trasmissione_finita = self.gestisci_fine_trasmissione
    
    # Roba per la trascrizione
    def esegui_analisi(self, file_mp3):
        print(f"Analisi AI STT iniziata per {file_mp3}...")
        self.testo = self.stt.startTranscibe(file_mp3)
        if not self.testo:
            return
        
        # Qua facciamo il pathing per le varie cartelle, input_transcript
        os.makedirs("input_transcript", exist_ok=True)
        nome_base = os.path.splitext(os.path.basename(file_mp3))[0]  # es: record_001
        transcript_path = os.path.join("input_transcript", f"{nome_base}.txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(self.testo)

        # Ollama analizza il transcript
        risultato = self.ollama.analisiFile(self.testo)
        print(f"RISULTATO AI: {risultato}")

        # 4. Sposta il transcript in already_processed_transcript
        os.makedirs("already_processed_transcript", exist_ok=True)
        shutil.move(transcript_path, os.path.join("already_processed_transcript", f"{nome_base}.txt"))
        
    def gestisci_fine_trasmissione(self, file_mp3):
        thread_stt = threading.Thread(target=self.esegui_analisi, args=(file_mp3,))
        thread_stt.start()
    """
    # --- controlli trigger originale ---
    def setSquelch(self, valore):
        self.alt_audio.setSquelch(valore)

    def setSilenzioPostTrasm(self, secondi):
        self.alt_audio.setSilenzioPostTrasm(secondi)

    def stopListen(self):
        self.alt_audio.stopListen()

    def startListen(self):
        self.alt_audio.startListen()
    """
    # controlli Silero VAD 
    def setVadThreshold(self, valore):
        self.audio.setVadThreshold(valore)

    def stopListenVad(self):
        self.audio.stopListen()
        self.audio_worker.wait() 

    def startListenVad(self):
        self.audio_worker = AudioWorker(self.audio)
        self.audio_worker.start()
