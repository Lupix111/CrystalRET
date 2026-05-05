from faster_whisper import WhisperModel
import os

class STT:
    
    def __init__(self):
        self.model_size = "tiny"
        self.model = WhisperModel(self.model_size, device="cuda", compute_type="int8_float16")

    def setModel(self, modelSize):
        if modelSize in ["tiny","base","small","medium","large-v1","large-v2","large-v3","large-v3-turbo","distil-large-v2","distil-large-v3"]:
            self.model_size=modelSize
            self.model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)
        else:
            print("The model does not exist.")

    def startTranscibe(self, file_mp3_path):
        segments, info = self.model.transcribe(file_mp3_path, beam_size=5, language="it")
        
        full_text = ""
        for segment in segments:
            full_text += segment.text + " "
            
        return full_text.strip()
