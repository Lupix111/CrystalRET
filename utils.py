import sys
import os


def get_base_dir() -> str:
    """
    Restituisce la cartella base del programma
    - In sviluppo: cartella del progetto
    - Con PyInstaller: cartella dell'exe
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))