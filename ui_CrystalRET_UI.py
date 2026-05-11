# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrystalRET_UIPbwbjg.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        icon = QIcon()
        icon.addFile(u":/Main/main_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBoxopzioni = QGroupBox(self.centralwidget)
        self.groupBoxopzioni.setObjectName(u"groupBoxopzioni")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxopzioni)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_monitoraggio = QPushButton(self.groupBoxopzioni)
        self.pushButton_monitoraggio.setObjectName(u"pushButton_monitoraggio")

        self.horizontalLayout_4.addWidget(self.pushButton_monitoraggio)

        self.pushButton_pausa = QPushButton(self.groupBoxopzioni)
        self.pushButton_pausa.setObjectName(u"pushButton_pausa")

        self.horizontalLayout_4.addWidget(self.pushButton_pausa)

        self.pushButton_esportalog = QPushButton(self.groupBoxopzioni)
        self.pushButton_esportalog.setObjectName(u"pushButton_esportalog")

        self.horizontalLayout_4.addWidget(self.pushButton_esportalog)

        self.pushButton_impostazioni = QPushButton(self.groupBoxopzioni)
        self.pushButton_impostazioni.setObjectName(u"pushButton_impostazioni")

        self.horizontalLayout_4.addWidget(self.pushButton_impostazioni)


        self.gridLayout_2.addWidget(self.groupBoxopzioni, 0, 0, 1, 3)

        self.groupBoxTrascrizioni = QGroupBox(self.centralwidget)
        self.groupBoxTrascrizioni.setObjectName(u"groupBoxTrascrizioni")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxTrascrizioni)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.trascrizioni = QTableWidget(self.groupBoxTrascrizioni)
        self.trascrizioni.setObjectName(u"trascrizioni")
        self.trascrizioni.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.verticalLayout_3.addWidget(self.trascrizioni)


        self.gridLayout_2.addWidget(self.groupBoxTrascrizioni, 1, 1, 1, 1)

        self.groupBoxSegnaleStato = QGroupBox(self.centralwidget)
        self.groupBoxSegnaleStato.setObjectName(u"groupBoxSegnaleStato")
        self.groupBoxSegnaleStato.setMaximumSize(QSize(300, 16777215))
        self.gridLayout = QGridLayout(self.groupBoxSegnaleStato)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxAudioLev = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxAudioLev.setObjectName(u"groupBoxAudioLev")
        self.groupBoxAudioLev.setMaximumSize(QSize(16777215, 75))
        self.gridLayout_3 = QGridLayout(self.groupBoxAudioLev)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.livello_audio = QProgressBar(self.groupBoxAudioLev)
        self.livello_audio.setObjectName(u"livello_audio")
        self.livello_audio.setMinimumSize(QSize(0, 30))
        self.livello_audio.setValue(0)
        self.livello_audio.setTextVisible(False)

        self.gridLayout_3.addWidget(self.livello_audio, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBoxAudioLev, 2, 0, 1, 1)

        self.groupBoxStatusReg = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxStatusReg.setObjectName(u"groupBoxStatusReg")
        self.groupBoxStatusReg.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.groupBoxStatusReg)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelStatusReg = QLabel(self.groupBoxStatusReg)
        self.labelStatusReg.setObjectName(u"labelStatusReg")

        self.horizontalLayout.addWidget(self.labelStatusReg)

        self.labelTimerReg = QLabel(self.groupBoxStatusReg)
        self.labelTimerReg.setObjectName(u"labelTimerReg")

        self.horizontalLayout.addWidget(self.labelTimerReg)


        self.gridLayout.addWidget(self.groupBoxStatusReg, 3, 0, 1, 1)

        self.groupBoxFreq = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxFreq.setObjectName(u"groupBoxFreq")
        self.groupBoxFreq.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_6 = QVBoxLayout(self.groupBoxFreq)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lcdFrequenza = QLCDNumber(self.groupBoxFreq)
        self.lcdFrequenza.setObjectName(u"lcdFrequenza")
        self.lcdFrequenza.setSmallDecimalPoint(True)
        self.lcdFrequenza.setDigitCount(6)
        self.lcdFrequenza.setMode(QLCDNumber.Mode.Dec)
        self.lcdFrequenza.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.lcdFrequenza.setProperty(u"value", 145500.000000000000000)

        self.verticalLayout_6.addWidget(self.lcdFrequenza)

        self.spinBoxFrequenza = QDoubleSpinBox(self.groupBoxFreq)
        self.spinBoxFrequenza.setObjectName(u"spinBoxFrequenza")
        self.spinBoxFrequenza.setDecimals(0)
        self.spinBoxFrequenza.setMaximum(999999.000000000000000)
        self.spinBoxFrequenza.setValue(145500.000000000000000)

        self.verticalLayout_6.addWidget(self.spinBoxFrequenza)


        self.gridLayout.addWidget(self.groupBoxFreq, 0, 0, 1, 1)

        self.groupBoxSlider = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxSlider.setObjectName(u"groupBoxSlider")
        self.groupBoxSlider.setMaximumSize(QSize(16777215, 125))
        self.verticalLayout_5 = QVBoxLayout(self.groupBoxSlider)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.groupBoxSlider)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.horizontalSliderSquelch = QSlider(self.groupBoxSlider)
        self.horizontalSliderSquelch.setObjectName(u"horizontalSliderSquelch")
        self.horizontalSliderSquelch.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSliderSquelch)

        self.label_2 = QLabel(self.groupBoxSlider)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.horizontalSliderSilenzioTime = QSlider(self.groupBoxSlider)
        self.horizontalSliderSilenzioTime.setObjectName(u"horizontalSliderSilenzioTime")
        self.horizontalSliderSilenzioTime.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSliderSilenzioTime)


        self.gridLayout.addWidget(self.groupBoxSlider, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBoxSegnaleStato, 1, 0, 1, 1)

        self.groupBoxAi = QGroupBox(self.centralwidget)
        self.groupBoxAi.setObjectName(u"groupBoxAi")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxAi)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.OllamaLog = QTextEdit(self.groupBoxAi)
        self.OllamaLog.setObjectName(u"OllamaLog")
        self.OllamaLog.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.verticalLayout_2.addWidget(self.OllamaLog)

        self.systemPromptlabel = QLabel(self.groupBoxAi)
        self.systemPromptlabel.setObjectName(u"systemPromptlabel")

        self.verticalLayout_2.addWidget(self.systemPromptlabel)

        self.promptEdit = QTextEdit(self.groupBoxAi)
        self.promptEdit.setObjectName(u"promptEdit")
        self.promptEdit.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_2.addWidget(self.promptEdit)


        self.gridLayout_2.addWidget(self.groupBoxAi, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxopzioni.setTitle(QCoreApplication.translate("MainWindow", u"Opzioni", None))
        self.pushButton_monitoraggio.setText(QCoreApplication.translate("MainWindow", u"Monitoraggio", None))
        self.pushButton_pausa.setText(QCoreApplication.translate("MainWindow", u"Pausa", None))
        self.pushButton_esportalog.setText(QCoreApplication.translate("MainWindow", u"Esporta Log", None))
        self.pushButton_impostazioni.setText(QCoreApplication.translate("MainWindow", u"Impostazioni", None))
        self.groupBoxTrascrizioni.setTitle(QCoreApplication.translate("MainWindow", u"Log Trasmissioni", None))
        self.groupBoxSegnaleStato.setTitle(QCoreApplication.translate("MainWindow", u"Segnale e Stato", None))
        self.groupBoxAudioLev.setTitle(QCoreApplication.translate("MainWindow", u"Livello Audio (dBFS)", None))
        self.groupBoxStatusReg.setTitle(QCoreApplication.translate("MainWindow", u"Status Registrazione", None))
        self.labelStatusReg.setText(QCoreApplication.translate("MainWindow", u"In ascolto", None))
        self.labelTimerReg.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.groupBoxFreq.setTitle(QCoreApplication.translate("MainWindow", u"Frequenza (MHz)", None))
        self.spinBoxFrequenza.setSuffix(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.groupBoxSlider.setTitle(QCoreApplication.translate("MainWindow", u"Trigger Audio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Soglia Squelch", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Silenzio post-TX", None))
        self.groupBoxAi.setTitle(QCoreApplication.translate("MainWindow", u"Analisi AI", None))
        self.systemPromptlabel.setText(QCoreApplication.translate("MainWindow", u"System Prompt", None))
        self.promptEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Inserisci il system prompt per Ollama...", None))
    # retranslateUi

