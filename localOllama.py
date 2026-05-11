import ollama
import os, sys
import shutil
import requests
import subprocess
import time
from PySide6.QtWidgets import QMessageBox
import webbrowser



models = ["mistral","orca-mini","phi-2"]

def _get_base_dir() -> str:
    """Restituisce la cartella base sia in sviluppo che con PyInstaller"""
    if getattr(sys, 'frozen', False):
        # siamo dentro l'exe PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # siamo in sviluppo normale
        return os.path.dirname(os.path.abspath(__file__))

class LocalOllama:
    def __init__(self):
        base = _get_base_dir()
        self.path             = os.path.join(base, "input_transcript")
        self.alreadyProcessed = os.path.join(base, "already_processed_transcript")
        os.makedirs(self.path, exist_ok=True)
        os.makedirs(self.alreadyProcessed, exist_ok=True)
        self.dir_list = os.listdir(self.path)  #  Valutato all'istanza, non alla classe
        self.currentmodel = "mistral"
        self.prompt = "Find anything in this text that looks like an italian HAM Radio call-sign and only write that: "


    def _check_ollama(self):
        """Controlla se Ollama è raggiungibile, altrimenti prova ad avviarlo."""
        try:
            r = requests.get("http://localhost:11434", timeout=2)
            if r.status_code == 200:
                print("Ollama: online.")
                return True
        except requests.exceptions.ConnectionError:
            pass
        
        msg = QMessageBox()
        msg.setWindowTitle("Ollama non trovato")
        msg.setText("Ollama non è installato o non è raggiungibile. Se ha installato Ollama ma non l'hai aperto chiudi questa finestra.")
        msg.setInformativeText("Vuoi aprire la pagina di download di Ollama?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if msg.exec() == QMessageBox.StandardButton.Yes:
            webbrowser.open("https://ollama.com/download")
            return False
    
        # Ollama non risponde, prova ad avviarlo
        print("Ollama non raggiungibile, avvio in corso...")
        try:
            subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            # aspetta che si avvii
            time.sleep(3)
            r = requests.get("http://localhost:11434", timeout=2)
            if r.status_code == 200:
                print("Ollama avviato correttamente.")
                return True
        except Exception as e:
            print(f"Impossibile avviare Ollama: {e}")
            return False

    def analisiFile(self, testo):
        result = ollama.generate(
            model=self.currentmodel,
            prompt=f"{self.prompt}{testo}"
        )
        return result['response']
    
    def analisiGeneraleTesti(self):
        for nome_file in self.dir_list:
            full_path = os.path.join(self.path, nome_file)  #  Path completo
            with open(full_path, 'r', encoding='utf-8') as f:  #  Legge il contenuto
                testo = f.read()
            self.analisiFile(testo)  
            shutil.move(full_path, self.alreadyProcessed)  #  Path completo

    def setPath(self, newPath):
        self.path = newPath + "CrystalRET\\input_transcript"
        self.alreadyProcessed = newPath + "CrystalRET\\already_processed_transcripts"
    
    def setModel (self, model):
        if model in models:
            self.currentmodel = model
        else:
            print("No such model available, please try again")    


