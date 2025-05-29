from PyQt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interp.ui")z

app = QApplication([])
window = MainWindow()
window.show()
app.exec()