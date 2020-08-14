from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"C:\Users\emay\Documents\GitHub\Egzersizler\Selim\USI\untitled.ui")
        self.win.btGiris.clicked.connect(self.giris)
        self.win.btIptal.clicked.connect(self.temizle)
        self.win.show()

    def giris(self):
        user = self.win.txtKulalaniciAdi.text()
        password = self.win.txtSifre.text()
        print(user,password)

    def temizle(self):
        self.win.txtKulalaniciAdi.setText("")
        self.win.txtSifre.setText("")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())