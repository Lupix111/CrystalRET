import sys
import os

if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')

# ora importa tutto il resto
from guiImp import guiImp
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = guiImp()
    window.show()
    sys.exit(app.exec())