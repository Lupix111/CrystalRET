import threading
import STT
import audioTrigger

def esegui_analisi(self, file_mp3):
    """Questa funzione gira 'dietro le quinte' (in background)"""
    print(f"Analisi AI iniziata per {file_mp3}...")
    
    # 1. Trascrizione con la classe STT
    testo = self.stt_engine.transcribe_file(file_mp3)
    
    if testo:
        print(f"RISULTATO AI: {testo}")
        # 2. Qui chiamerai Ollama per il nominativo (prossimo step)
        # 3. Log su file di testo
        with open("log_radio.txt", "a") as f:
            f.write(f"[{file_mp3}] {testo}\n")

def gestisci_fine_trasmissione(self, file_mp3):
    """Viene chiamato appena il file MP3 è pronto"""
    
    # Creiamo un Thread che si occupa della trascrizione
    # così il loop principale della radio non si ferma!
    thread_stt = threading.Thread(target=self.esegui_analisi, args=(file_mp3,))
    thread_stt.start()