from PySide6 import QtWidgets
from PySide6  import QtCore
from ui_CrystalRET_UI import Ui_MainWindow  
import sys

class guiImp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_monitoraggio.clicked.connect()
        self.pushButton_pausa.clicked.connect()
        self.pushButton_esportalog.clicked.connect()
        self.pushButton_impostazioni.clicked.connect()  
    
if __name__  == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    window = guiImp()
    window.show()
    sys.exit(app.exec())


        
