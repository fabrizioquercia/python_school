from PyQt6.QtWidgets import *
from PyQt6.uic import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interp.ui")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()