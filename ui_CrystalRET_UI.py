# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrystalRET_UIcQyYXK.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(896, 683)
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
        self.verticalLayout = QVBoxLayout(self.groupBoxSegnaleStato)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxFreq = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxFreq.setObjectName(u"groupBoxFreq")
        self.lcdFrequenza = QLCDNumber(self.groupBoxFreq)
        self.lcdFrequenza.setObjectName(u"lcdFrequenza")
        self.lcdFrequenza.setGeometry(QRect(20, 10, 231, 81))
        self.lcdFrequenza.setDigitCount(6)
        self.lcdFrequenza.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.lcdFrequenza.setProperty(u"value", 145500.000000000000000)

        self.verticalLayout.addWidget(self.groupBoxFreq)

        self.groupBoxAudioLev = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxAudioLev.setObjectName(u"groupBoxAudioLev")
        self.verticalLayout_4 = QVBoxLayout(self.groupBoxAudioLev)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.livello_audio = QProgressBar(self.groupBoxAudioLev)
        self.livello_audio.setObjectName(u"livello_audio")
        self.livello_audio.setValue(24)

        self.verticalLayout_4.addWidget(self.livello_audio)


        self.verticalLayout.addWidget(self.groupBoxAudioLev)

        self.groupBoxSquelch = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxSquelch.setObjectName(u"groupBoxSquelch")
        self.progressBar_2 = QProgressBar(self.groupBoxSquelch)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(70, 60, 118, 23))
        self.progressBar_2.setValue(24)
        self.horizontalSlider_3 = QSlider(self.groupBoxSquelch)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setGeometry(QRect(60, 60, 160, 16))
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.groupBoxSquelch)

        self.groupBoxStatusReg = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxStatusReg.setObjectName(u"groupBoxStatusReg")

        self.verticalLayout.addWidget(self.groupBoxStatusReg)

        self.groupBoxSlider = QGroupBox(self.groupBoxSegnaleStato)
        self.groupBoxSlider.setObjectName(u"groupBoxSlider")
        self.verticalLayout_5 = QVBoxLayout(self.groupBoxSlider)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSliderSquelch = QSlider(self.groupBoxSlider)
        self.horizontalSliderSquelch.setObjectName(u"horizontalSliderSquelch")
        self.horizontalSliderSquelch.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSliderSquelch)

        self.horizontalSliderSilenzioTime = QSlider(self.groupBoxSlider)
        self.horizontalSliderSilenzioTime.setObjectName(u"horizontalSliderSilenzioTime")
        self.horizontalSliderSilenzioTime.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSliderSilenzioTime)


        self.verticalLayout.addWidget(self.groupBoxSlider)


        self.gridLayout_2.addWidget(self.groupBoxSegnaleStato, 1, 0, 1, 1)

        self.groupBoxAi = QGroupBox(self.centralwidget)
        self.groupBoxAi.setObjectName(u"groupBoxAi")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxAi)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.OllamaLog = QTextEdit(self.groupBoxAi)
        self.OllamaLog.setObjectName(u"OllamaLog")
        self.OllamaLog.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.verticalLayout_2.addWidget(self.OllamaLog)

        self.label = QLabel(self.groupBoxAi)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


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
        self.groupBoxFreq.setTitle(QCoreApplication.translate("MainWindow", u"Frequenza (MHz)", None))
        self.groupBoxAudioLev.setTitle(QCoreApplication.translate("MainWindow", u"Livello Audio (dBFS)", None))
        self.groupBoxSquelch.setTitle(QCoreApplication.translate("MainWindow", u"Squelch", None))
        self.groupBoxStatusReg.setTitle(QCoreApplication.translate("MainWindow", u"Status Registrazione", None))
        self.groupBoxSlider.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBoxAi.setTitle(QCoreApplication.translate("MainWindow", u"Analisi AI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

