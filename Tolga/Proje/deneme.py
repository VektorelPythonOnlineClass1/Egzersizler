import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Calibri")

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buton oluşturma")
        self.setGeometry(40,40,400,400)
        self.arayuz

    def arayuz(self):
        self.yazi = QLabel("Merhaba python",self)
        self.yazi.setFont(font)
        self.yazi.move(160,80)
        self.buton1 = QPushButton("Giriş",self)
        self.buton2 = QPushButton("Çıkış", self)
        self.buton2.move(240,80)
        self.buton2.setFont(font)
        
        self.show()

uygulama = QApplication(sys.argv)

pencere = Pencere()
sys.exit(uygulama.exec_())




