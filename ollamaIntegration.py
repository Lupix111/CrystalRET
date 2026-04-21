import ollama
import os
import shutil


models = ["mistral","orca-mini","phi-2"]

class LocalOllama():

    def __init__(self):
        self.path = "C:\\Users\\em4nc\\OneDrive\\Desktop\\Python\\CrystalRET\\input_transcript"
        self.alreadyProcessed = "C:\\Users\\em4nc\\OneDrive\\Desktop\\Python\\CrystalRET\\already_processed_transcripts"
        self.dir_list = os.listdir(self.path)  #  Valutato all'istanza, non alla classe
        self.currentmodel = "mistral"

    def analisiFile(self, testo):
        prompt = f"Find anything in this text that looks like a HAM Radio call-sign and only write that:{testo}"
        result = ollama.generate(model=self.currentmodel, prompt=prompt)
        print("CALLSIGN:", result['response'])

    def analisiTestiOllama(self):
        for nome_file in self.dir_list:
            full_path = os.path.join(self.path, nome_file)  #  Path completo
            with open(full_path, 'r', encoding='utf-8') as f:  #  Legge il contenuto
                testo = f.read()
            self.analisiFile(testo)  #  self.analisiFile, non ollama.analisiFile
            shutil.move(full_path, self.alreadyProcessed)  #  Path completo
    
    def setModel (self, model):
        if model in models:
            self.currentmodel = model
        else:
            print("No such model available, please try again")    

test = LocalOllama()
test.analisiTestiOllama()
