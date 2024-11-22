import sys
from PyQt5.QtWidgets import QApplication
from src.interface import CryptoApp

def main():
    """
    Fonction principale qui initialise et lance l'application de cryptographie.
    """
    app = QApplication(sys.argv)
    crypto_app = CryptoApp()
    crypto_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
