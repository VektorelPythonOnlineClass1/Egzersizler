from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,uic
import sys
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"Ibrahim\ilk.ui")
        self.win.btDugme.clicked.connect(self.tiklandi)
        self.win.show()

    def tiklandi(self):
        self.win.txtSonuc.setText("Tıklandı")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyg = App()
    sys.exit(app.exec_())