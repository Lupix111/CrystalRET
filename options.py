from PySide6.QtCore import QSettings

class options:
    def __init__(self):
        self.qs = QSettings("CrystalRET", "RadioMonitor")

    def load(self):
        return {
            "vad_threshold ":       self.qs.value("vad_threshold ", 500),
            "silenzio":     self.qs.value("silenzio", 2.0),
            "model_stt":    self.qs.value("model_stt", "tiny"),
            "model_ollama": self.qs.value("model_ollama", "mistral"),
            "prompt":       self.qs.value("prompt", "Analizza questa trasmissione radio.")
        }

    def save(self, config: dict):
        for key, value in config.items():
            self.qs.setValue(key, value)