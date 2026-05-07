from faster_whisper import WhisperModel
import os

class STT:
    
    def __init__(self):
        self.model_size = "tiny"
        self.device        = "cuda"
        self.compute_type  = "int8_float16"
        self.model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)

    def setModel(self, model_size: str):
        valid = ["tiny", "base", "small", "medium",
                 "large-v1", "large-v2", "large-v3",
                 "large-v3-turbo", "distil-large-v2", "distil-large-v3"]
        if model_size in valid:
            self.model_size = model_size
            self.model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)
        else:
            print(f"Modello non valido: {model_size}")

    def startTranscibe(self, file_mp3_path: str) -> str:
        segments, info = self.model.transcribe(file_mp3_path, beam_size=5, language="it")
        full_text = " ".join(segment.text for segment in segments)
        return full_text.strip()
