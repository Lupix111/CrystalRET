import pyaudio
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout,
                                QLabel, QComboBox, QPushButton, QGroupBox)


WHISPER_MODELS = ["tiny", "base", "small", "medium",
                  "large-v1", "large-v2", "large-v3",
                  "large-v3-turbo", "distil-large-v2", "distil-large-v3"]

OLLAMA_MODELS  = ["mistral", "orca-mini", "phi-2"]


class dialogImpostazioni(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle("Impostazioni")
        self.setMinimumWidth(380)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        layout.addWidget(self._group_audio())
        layout.addWidget(self._group_whisper())
        layout.addWidget(self._group_ollama())
        layout.addLayout(self._buttons())

    #GRUPPI#

    def _group_audio(self) -> QGroupBox:
        group = QGroupBox("Dispositivo audio input")
        layout = QVBoxLayout(group)

        self.combo_audio = QComboBox()
        self._popola_dispositivi()
        layout.addWidget(self.combo_audio)

        return group

    def _group_whisper(self) -> QGroupBox:
        group = QGroupBox("Modello Whisper")
        layout = QVBoxLayout(group)

        self.combo_whisper = QComboBox()
        self.combo_whisper.addItems(WHISPER_MODELS)

        # seleziona il modello attualmente in uso
        modello_corrente = self.controller.stt.model_size
        if modello_corrente in WHISPER_MODELS:
            self.combo_whisper.setCurrentText(modello_corrente)

        layout.addWidget(self.combo_whisper)
        return group

    def _group_ollama(self) -> QGroupBox:
        group = QGroupBox("Modello Ollama")
        layout = QVBoxLayout(group)

        self.combo_ollama = QComboBox()
        self.combo_ollama.addItems(OLLAMA_MODELS)

        # seleziona il modello attualmente in uso
        modello_corrente = self.controller.ollama.currentmodel
        if modello_corrente in OLLAMA_MODELS:
            self.combo_ollama.setCurrentText(modello_corrente)

        layout.addWidget(self.combo_ollama)
        return group

    def _buttons(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.addStretch()

        btn_annulla = QPushButton("Annulla")
        btn_annulla.clicked.connect(self.reject)

        btn_salva = QPushButton("Salva")
        btn_salva.setDefault(True)
        btn_salva.clicked.connect(self._salva)

        layout.addWidget(btn_annulla)
        layout.addWidget(btn_salva)
        return layout

    
    #LOGICA#

    def _popola_dispositivi(self):
        """Popola la combobox con i dispositivi di input disponibili."""
        self.combo_audio.clear()
        self._devices = self.controller.audio.get_input_devices()
        for dev in self._devices:
            self.combo_audio.addItem(dev["name"], userData=dev["index"])

        # seleziona il device attualmente in uso
        current_index = self.controller.audio.device_index
        for i, dev in enumerate(self._devices):
            if dev["index"] == current_index:
                self.combo_audio.setCurrentIndex(i)
                break

    def _salva(self):
        """Applica le impostazioni al controller e chiude il dialog."""
        # dispositivo audio
        device_index = self.combo_audio.currentData()
        self.controller.audio.setDeviceIndex(device_index)

        # modello Whisper
        whisper_model = self.combo_whisper.currentText()
        self.controller.stt.setModel(whisper_model)

        # modello Ollama
        ollama_model = self.combo_ollama.currentText()
        self.controller.ollama.setModel(ollama_model)

        self.accept()