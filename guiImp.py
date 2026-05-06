from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from ui_CrystalRET_UI import Ui_MainWindow
import sys
import os
import datetime
from radioController import radioController


class guiImp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = radioController()
        self._setup_trascrizioni()
        self._setup_slider_labels()
        self._connect_signals()
        self._update_status("Pronto.")

    #SETUP INIZIALE#

    def _setup_trascrizioni(self):
        """Configura le colonne della tabella log."""
        self.trascrizioni.setColumnCount(4)
        self.trascrizioni.setHorizontalHeaderLabels(["Ora", "Durata", "Stato", "Trascrizione"])
        self.trascrizioni.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.trascrizioni.setEditTriggers(self.trascrizioni.EditTrigger.NoEditTriggers)
        self.trascrizioni.setSelectionBehavior(self.trascrizioni.SelectionBehavior.SelectRows)
        self.trascrizioni.verticalHeader().setVisible(False)
        self.trascrizioni.itemSelectionChanged.connect(self._on_riga_selezionata)

    def _setup_slider_labels(self):
        """Imposta i range degli slider."""
        self.horizontalSliderSquelch.setMinimum(0)
        self.horizontalSliderSquelch.setMaximum(200)
        self.horizontalSliderSquelch.setValue(60)

        self.horizontalSliderSilenzioTime.setMinimum(1)
        self.horizontalSliderSilenzioTime.setMaximum(10)
        self.horizontalSliderSilenzioTime.setValue(2)

    def _connect_signals(self):
        """Connette tutti i segnali ai rispettivi slot."""
        self.pushButton_monitoraggio.clicked.connect(self._on_monitoraggio)
        self.pushButton_pausa.clicked.connect(self._on_pausa)
        self.pushButton_esportalog.clicked.connect(self._on_esporta_log)
        self.pushButton_impostazioni.clicked.connect(self._on_impostazioni)

        self.horizontalSliderSquelch.valueChanged.connect(self._on_soglia_changed)
        self.horizontalSliderSilenzioTime.valueChanged.connect(self._on_silenzio_changed)

        self.trascrizioni.currentCellChanged.connect(self._on_riga_selezionata)

    #SLOT PULSANTI TOOLBAR#

    def _on_monitoraggio(self):
        """Avvia il monitoraggio radio."""
        self.controller.startListen()
        self._update_status("Monitoraggio avviato.")
        self.pushButton_monitoraggio.setEnabled(False)
        self.pushButton_pausa.setEnabled(True)

    def _on_pausa(self):
        """Mette in pausa il monitoraggio."""
        self.controller.stopListen()
        self._update_status("Monitoraggio fermato.")
        self.pushButton_monitoraggio.setEnabled(True)
        self.pushButton_pausa.setEnabled(False)

    def _on_esporta_log(self):
        """Esporta il log trascrizioni in un file di testo."""
        os.makedirs("log_files", exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join("log_files", f"log_{timestamp}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            for row in range(self.trascrizioni.rowCount()):
                ora      = self.trascrizioni.item(row, 0).text()
                durata   = self.trascrizioni.item(row, 1).text()
                stato    = self.trascrizioni.item(row, 2).text()
                testo    = self.trascrizioni.item(row, 3).text()
                f.write(f"[{ora}] ({durata}) [{stato}] {testo}\n")
        self._update_status(f"Log esportato: {filename}")

    def _on_impostazioni(self):
        """Apre il pannello impostazioni."""
        # TODO: aprire QDialog impostazioni
        self._update_status("Impostazioni (TODO).")

    #SLOT SLIDER#

    def _on_soglia_changed(self, valore):
        """Aggiorna la soglia squelch."""
        self.controller.audio.setSquelch(valore)
        self._update_status(f"Soglia squelch: {valore}")

    def _on_silenzio_changed(self, valore):
        """Aggiorna i secondi di silenzio post-trasmissione."""
        self.controller.audio.setSilenzioPostTrasm(valore)
        self._update_status(f"Silenzio post-TX: {valore}s")

    #SLOT TABELLA#

    def _on_riga_selezionata(self):
        """Quando si clicca una riga, mostra la risposta AI nel pannello destro."""
        riga = self.trascrizioni.currentRow()
        if riga < 0:
            return
        item_testo = self.trascrizioni.item(riga, 3)
        if item_testo:
            self.OllamaLog.setPlainText(f"Trascrizione selezionata:\n{item_testo.text()}")

    #METODI PUBBLICI chiamati da RadioController via Signal#

    def on_new_transcription(self, testo: str, durata: float):
        """
        Aggiunge una nuova riga al log trascrizioni.
        Collegare a: controller.transcription_ready
        """
        ora     = datetime.datetime.now().strftime("%H:%M:%S")
        dur_str = f"0:{int(durata):02d}"
        row     = self.trascrizioni.rowCount()
        self.trascrizioni.insertRow(row)

        self.trascrizioni.setItem(row, 0, QTableWidgetItem(ora))
        self.trascrizioni.setItem(row, 1, QTableWidgetItem(dur_str))

        stato_item = QTableWidgetItem("TX")
        stato_item.setForeground(QColor("#50c070"))
        self.trascrizioni.setItem(row, 2, stato_item)

        self.trascrizioni.setItem(row, 3, QTableWidgetItem(testo))
        self.trascrizioni.scrollToBottom()
        self._update_status(f"Nuova trascrizione ricevuta ({dur_str})")

    def on_ai_response(self, risposta: str):
        """
        Mostra la risposta di Ollama nel pannello destro.
        Collegare a: controller.ai_response_ready
        """
        ora = datetime.datetime.now().strftime("%H:%M:%S")
        self.OllamaLog.append(f"[{ora}]\n{risposta}\n{'─'*40}\n")

        # Aggiorna lo stato dell'ultima riga come "AI analizzata"
        ultima_riga = self.trascrizioni.rowCount() - 1
        if ultima_riga >= 0:
            stato_item = QTableWidgetItem("TX+AI")
            stato_item.setForeground(QColor("#5070e0"))
            self.trascrizioni.setItem(ultima_riga, 2, stato_item)

    def on_livello_audio(self, valore: int):
        """
        Aggiorna la VU bar del livello audio (0-100).
        Collegare a: controller.audio_level_changed
        """
        self.livello_audio.setValue(valore)

    def on_squelch_status(self, aperto: bool):
        """
        Aggiorna la progress bar squelch e il gruppo Status Registrazione.
        Collegare a: controller.squelch_changed
        """
        self.progressBar_2.setValue(100 if aperto else 0)
        self.groupBoxStatusReg.setTitle(
            "Status Registrazione — ● REC" if aperto else "Status Registrazione — In ascolto"
        )

    def on_model_changed(self, model_name: str):
        """Aggiorna la label del modello Ollama attivo."""
        self.label.setText(f"Modello: {model_name}")

    #UTILITY#

    def _update_status(self, messaggio: str):
        """Scrive un messaggio nella status bar in basso."""
        self.statusbar.showMessage(messaggio)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = guiImp()
    window.show()
    sys.exit(app.exec())
