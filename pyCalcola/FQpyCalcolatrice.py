import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class Calcolatrice(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("FQpyCalcolatrice.ui", self)
        self.btnPiu.clicked.connect(self.somma)
        self.btnMeno.clicked.connect(self.sottrai)
        self.btnPer.clicked.connect(self.moltiplica)
        self.btnDiviso.clicked.connect(self.dividi)

    def leggi_valori(self):
        try:
            val1 = float(self.txt1.toPlainText())
            val2 = float(self.txt2.toPlainText())
            return val1, val2
        except ValueError:
            self.txtRisultato.setText("Valori non validi")
            return None, None

    def somma(self):
        val1, val2 = self.leggi_valori()
        if val1 is not None:
            self.txtRisultato.setText("+ = "+str(val1 + val2))

    def sottrai(self):
        val1, val2 = self.leggi_valori()
        if val1 is not None:
            self.txtRisultato.setText("- = "+str(val1 - val2))

    def moltiplica(self):
        val1, val2 = self.leggi_valori()
        if val1 is not None:
            self.txtRisultato.setText("x = "+str(val1 * val2))

    def dividi(self):
        val1, val2 = self.leggi_valori()
        if val1 is not None:
            if val2 == 0:
                self.txtRisultato.setText("Errore: divisione per zero")
            else:
                self.txtRisultato.setText(": = "+str(val1 / val2))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calcolatrice()
    window.show()
    sys.exit(app.exec())