import threading
from STT import STT
from audioTrigger import audioTrigger
from localOllama import LocalOllama

class radioController:
    def __init__(self):
        self.audio = audioTrigger()
        self.stt = STT()
        self.testo = ""
        self.ollama = LocalOllama()

    def esegui_analisi(self, file_mp3):
        #Questa funzione gira in background
        print(f"Analisi AI iniziata per {file_mp3}...")
        
        # 1. Trascrizione con la classe STT
        self.stt = STT()
        self.testo = self.stt.startTranscibe(file_mp3)
        
        if self.testo:
            print(f"RISULTATO TRASCRIZIONE: {self.testo}")
            
            print(f"RISULTATO AI: {self.ollama.analisiFile(self.testo)}")
            # 3. Log su file di testo
            with open("log_radio.txt", "a") as f:
                f.write(f"[{file_mp3}] {self.testo}\n")

    def gestisci_fine_trasmissione(self, file_mp3):
        #viene chiamato appena il file MP3 è pronto
        
        # creiamo un Thread che si occupa della trascrizione
        # così il loop principale della radio non si ferma
        thread_stt = threading.Thread(target=self.esegui_analisi, args=(file_mp3,))
        thread_stt.start()

    def setSquelch(self, valore):
        self.audio.setSquelch(valore)
    
    def setSilenzioPostTrasm(self, secondi):
        self.audio.setSilenzioPostTrasm(secondi)

    def stopListen(self):
        self.audio.stopListen()
    
    def startListen(self):
        self.audio.startListen()