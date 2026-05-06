import threading
from STT import STT
from audioTrigger import audioTrigger
from localOllama import LocalOllama
from alternative_audioTrigger import alternative_audioTrigger
class radioController:
    def __init__(self):
        self.alt_audio = audioTrigger()
        self.stt = STT()
        self.testo = ""
        self.ollama = LocalOllama()
        self.audio = alternative_audioTrigger()

        # trigger con Silero VAD
        self.audio = alternative_audioTrigger()
        self.audio.on_trasmissione_finita = self.gestisci_fine_trasmissione
        
        # legacy — istanziare solo se si vuole tornare al trigger originale
        # self.audio = audioTrigger()
        # self.audio.on_trasmissione_finita = self.gestisci_fine_trasmissione

    def esegui_analisi(self, file_mp3):
        print(f"Analisi AI iniziata per {file_mp3}...")
        self.testo = self.stt.startTranscibe(file_mp3)
        if self.testo:
            print(f"RISULTATO TRASCRIZIONE: {self.testo}")
            print(f"RISULTATO AI: {self.ollama.analisiFile(self.testo)}")
            with open("log_radio.txt", "a") as f:
                f.write(f"[{file_mp3}] {self.testo}\n")

    def gestisci_fine_trasmissione(self, file_mp3):
        thread_stt = threading.Thread(target=self.esegui_analisi, args=(file_mp3,))
        thread_stt.start()

    # --- controlli trigger originale ---
    def setSquelch(self, valore):
        self.alt_audio.setSquelch(valore)

    def setSilenzioPostTrasm(self, secondi):
        self.alt_audio.setSilenzioPostTrasm(secondi)

    def stopListen(self):
        self.alt_audio.stopListen()

    def startListen(self):
        self.alt_audio.startListen()

    # controlli Silero VAD 
    def setVadThreshold(self, valore):
        self.audio.setVadThreshold(valore)

    def stopListenVad(self):
        self.audio.stopListen()

    def startListenVad(self):
        self.audio.startListen()
