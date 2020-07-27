from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"Ibrahim\Proje\UIS\Ana.ui")
        self.win.btGiris.clicked.connect(self.giris)
        self.win.btIptal.clicked.connect(self.temizle)
        self.win.show()

    def giris(self):
        user = self.win.txtUserInput.text()
        password = self.win.txtSifre.text()
        self.bot = InstagramBot(user,password,bekle=5)
        self.bot.girisYap()

    def temizle(self):
        self.win.txtUserInput.setText("")
        self.win.txtSifre.setText("")
        

class InstagramBot:
    def __init__(self,kullaniciAdi,sifre,bekle=5):
        self.kullaniciAdi = kullaniciAdi
        self.sifre = sifre
        self.bekle = bekle

    def girisYap(self):
        self.tarayici = webdriver.Firefox(executable_path=r"Ibrahim\Proje\Drivers\geckodriver.exe")
        self.tarayici.get(r"https://www.instagram.com/accounts/login")
        self.bekleme()
        eposta = self.tarayici.find_element_by_name("username")
        sifre = self.tarayici.find_element_by_name("password")
        self.bekleme()
        eposta.send_keys(self.kullaniciAdi)
        sifre.send_keys(self.sifre)
        sifre.send_keys(Keys.ENTER)
        self.bekleme()
        giris = self.tarayici.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        giris.click()
    def bekleme(self):
        time.sleep(self.bekle)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

