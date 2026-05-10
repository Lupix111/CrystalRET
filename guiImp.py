import sys
import os

# fix per PyInstaller --windowed: torch.hub scrive su stderr/stdout
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')

from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QDialog, QVBoxLayout, QTextEdit, QLabel
from PySide6.QtGui import QColor
from PySide6.QtCore import QTimer
from ui_CrystalRET_UI import Ui_MainWindow
import datetime
from radioController import radioController
from dialogImpostazioni import dialogImpostazioni
from utils import get_base_dir


class guiImp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = radioController()
        self.controller.transcription_ready.connect(self.on_new_transcription)
        self.controller.ai_response_ready.connect(self.on_ai_response)
        self._setup_trascrizioni()
        self._setup_slider_labels()
        self._setup_styles()  
        self._connect_signals()
        self._rec_timer = QTimer()
        self._rec_timer.timeout.connect(self._aggiorna_timer_rec)
        self._rec_seconds = 0
        self.controller.ollama._check_ollama()
        self._update_status("Pronto.")
        self.promptEdit.setText(self.controller.ollama.prompt)
        self.promptEdit.textChanged.connect(self._on_prompt_changed)
        self.spinBoxFrequenza.setValue(145.500)
        self.spinBoxFrequenza.valueChanged.connect(self._on_frequenza_changed)
        self.controller.squelch_changed.connect(self.on_squelch_status)
        self.controller.audio_level_changed.connect(self.on_livello_audio)

    # SETUP INIZIALE

    def _setup_trascrizioni(self):
        self.trascrizioni.setColumnCount(5)
        self.trascrizioni.setHorizontalHeaderLabels(["Ora", "Durata", "Freq (MHz)", "Stato", "Trascrizione"])
        self.trascrizioni.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        self.trascrizioni.setEditTriggers(self.trascrizioni.EditTrigger.NoEditTriggers)
        self.trascrizioni.setSelectionBehavior(self.trascrizioni.SelectionBehavior.SelectRows)
        self.trascrizioni.verticalHeader().setVisible(False)
        self.trascrizioni.itemSelectionChanged.connect(self._on_riga_selezionata)

    def _setup_slider_labels(self):
        self.horizontalSliderSquelch.setMinimum(0)
        self.horizontalSliderSquelch.setMaximum(100)
        self.horizontalSliderSquelch.setValue(60)
        self.horizontalSliderSilenzioTime.setMinimum(1)
        self.horizontalSliderSilenzioTime.setMaximum(10)
        self.horizontalSliderSilenzioTime.setValue(2)

    def _setup_styles(self):
        self.livello_audio.setMinimumHeight(25)
        self.livello_audio.setTextVisible(False)
        self.livello_audio.setStyleSheet("""
            QProgressBar {
                border: 1px solid #444;
                border-radius: 3px;
                background: #1a1c24;
            }
            QProgressBar::chunk {
                background: #3ddc6a;
                border-radius: 2px;
            }
        """)    

    def _connect_signals(self):
        self.pushButton_monitoraggio.clicked.connect(self._on_monitoraggio)
        self.pushButton_pausa.clicked.connect(self._on_pausa)
        self.pushButton_esportalog.clicked.connect(self._on_esporta_log)
        self.pushButton_impostazioni.clicked.connect(self._on_impostazioni)
        self.horizontalSliderSquelch.valueChanged.connect(self._on_soglia_changed)
        self.horizontalSliderSilenzioTime.valueChanged.connect(self._on_silenzio_changed)
        self.trascrizioni.currentCellChanged.connect(self._on_riga_selezionata)

    # SLOT PULSANTI TOOLBAR

    def _on_monitoraggio(self):
        self.controller.startListenVad()
        self._update_status("Monitoraggio avviato.")
        self.pushButton_monitoraggio.setEnabled(False)
        self.pushButton_pausa.setEnabled(True)

    def _on_pausa(self):
        self.controller.stopListenVad()
        self._update_status("Monitoraggio in pausa.")
        self.pushButton_monitoraggio.setEnabled(True)
        self.pushButton_pausa.setEnabled(False)

    def _on_esporta_log(self):
        log_dir = os.path.join(get_base_dir(), "log_files")
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename  = os.path.join(log_dir, f"log_{timestamp}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            for row in range(self.trascrizioni.rowCount()):
                ora    = self.trascrizioni.item(row, 0).text()
                durata = self.trascrizioni.item(row, 1).text()
                freq   = self.trascrizioni.item(row, 2).text()
                stato  = self.trascrizioni.item(row, 3).text()
                testo  = self.trascrizioni.item(row, 4).text()
                f.write(f"[{ora}] ({durata}) [{freq} MHz] [{stato}] {testo}\n")
        self._update_status(f"Log esportato: {filename}")

    def _on_impostazioni(self):
        dialog = dialogImpostazioni(self.controller, parent=self)
        dialog.exec()

    # SLOT SLIDER

    def _on_soglia_changed(self, valore):
        self.controller.audio.setVadThreshold(valore / 100)
        self._update_status(f"Soglia VAD: {valore}%")

    def _on_silenzio_changed(self, valore):
        self.controller.audio.setSilenzioPostTrasm(valore)
        self._update_status(f"Silenzio post-TX: {valore}s")

    # SLOT TABELLA

    def _on_riga_selezionata(self):
        riga = self.trascrizioni.currentRow()
        if riga < 0:
            return
        item_testo = self.trascrizioni.item(riga, 4)
        if not item_testo:
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Trascrizione")
        dialog.setMinimumSize(400, 200)
        layout = QVBoxLayout(dialog)

        ora   = self.trascrizioni.item(riga, 0).text()
        freq  = self.trascrizioni.item(riga, 2).text()
        label = QLabel(f"Trasmissione del {ora} — {freq} MHz")
        layout.addWidget(label)

        testo_edit = QTextEdit()
        testo_edit.setReadOnly(True)
        testo_edit.setText(item_testo.text())
        layout.addWidget(testo_edit)
        dialog.exec()

    # SLOT PROMPT

    def _on_prompt_changed(self):
        self.controller.ollama.prompt = self.promptEdit.toPlainText()

    # SLOT LCD FREQUENZA

    def _on_frequenza_changed(self, valore: float):
        self.lcdFrequenza.display(valore)

    # METODI PUBBLICI — chiamati via Signal dal controller

    def on_new_transcription(self, testo: str, durata: float):
        ora     = datetime.datetime.now().strftime("%H:%M:%S")
        dur_str = f"0:{int(durata):02d}"
        freq    = str(self.spinBoxFrequenza.value())
        row     = self.trascrizioni.rowCount()
        self.trascrizioni.insertRow(row)
        self.trascrizioni.setItem(row, 0, QTableWidgetItem(ora))
        self.trascrizioni.setItem(row, 1, QTableWidgetItem(dur_str))
        self.trascrizioni.setItem(row, 2, QTableWidgetItem(freq))
        stato_item = QTableWidgetItem("TX")
        stato_item.setForeground(QColor("#50c070"))
        self.trascrizioni.setItem(row, 3, stato_item)
        self.trascrizioni.setItem(row, 4, QTableWidgetItem(testo))
        self.trascrizioni.scrollToBottom()
        self._update_status(f"Nuova trascrizione ricevuta ({dur_str})")

    def on_ai_response(self, risposta: str):
        ora = datetime.datetime.now().strftime("%H:%M:%S")
        self.OllamaLog.append(f"[{ora}]\n{risposta}\n{'─'*40}\n")
        ultima_riga = self.trascrizioni.rowCount() - 1
        if ultima_riga >= 0:
            stato_item = QTableWidgetItem("TX+AI")
            stato_item.setForeground(QColor("#5070e0"))
            self.trascrizioni.setItem(ultima_riga, 3, stato_item)

    def on_livello_audio(self, valore: int):
        self.livello_audio.setValue(valore)

    def on_squelch_status(self, aperto: bool):
        if aperto:
            self._rec_seconds = 0
            self._rec_timer.start(1000)  # ogni secondo
            self.labelStatusReg.setText("● REC")
            self.labelStatusReg.setStyleSheet("color: red; font-weight: bold;")
        else:
            self._rec_timer.stop()
            self.labelStatusReg.setText("In ascolto")
            self.labelStatusReg.setStyleSheet("color: green;")
            self.labelTimerReg.setText("00:00")

    def _aggiorna_timer_rec(self):
        self._rec_seconds += 1
        minuti  = self._rec_seconds // 60
        secondi = self._rec_seconds % 60
        self.labelTimerReg.setText(f"{minuti:02d}:{secondi:02d}")

    def on_model_changed(self, model_name: str):
        self.label.setText(f"Modello: {model_name}")

    # UTILITY

    def _update_status(self, messaggio: str):
        self.statusbar.showMessage(messaggio)

    def closeEvent(self, event):
        self.controller.stopListenVad()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = guiImp()
    window.show()
    sys.exit(app.exec())