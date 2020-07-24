from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"Ibrahim\Proje\UIS\Ana.ui")
        self.win.btGiris.clicked.connect(self.giris)
        self.win.btIptal.clicked.connect(self.temizle)
        self.win.btFollow.clicked.connect(self.takipEt)
        self.win.btUnfollow.clicked.connect(self.takipBirak)
        self.win.btFollowList.clicked.connect(self.takipciListesi)
        self.win.show()

    def giris(self):
        user = self.win.txtUserInput.text()
        password = self.win.txtSifre.text()
        self.bot = InstagramBot(user,password,bekle=5)
        self.bot.girisYap()
        self.win.btFollow.setEnabled(True)
        self.win.btUnfollow.setEnabled(True)
        self.win.btFollowList.setEnabled(True)
        self.win.txtFollow.setEnabled(True)

    def temizle(self):
        self.win.txtUserInput.setText("")
        self.win.txtSifre.setText("")

    def takipEt(self):
        self.bot.takip(self.win.txtFollow.text())

    def takipBirak(self):
        self.bot.takibiBirak(self.win.txtFollow.text())

    def takipciListesi(self):
        self.bot.listeAl(self.win.txtFollow.text())

class InstagramBot:
    def __init__(self,kullaniciAdi,sifre,bekle=5):
        self.kullaniciAdi = kullaniciAdi
        self.sifre = sifre
        self.bekle = bekle
        self.tarayici = webdriver.Firefox(executable_path=r"Ibrahim\Proje\Drivers\geckodriver.exe")

    def girisYap(self):
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


    def takip(self,profileName,mod = 0):
        if mod:
            self.tarayici.get(profileName)
        else:
            self.tarayici.get(r"https://www.instagram.com/{0}".format(profileName))
        try:
            takipBt = self.tarayici.find_element_by_css_selector("button._5f5mN:nth-child(1)")
            if takipBt.text != "":
                takipBt.click()
                self.bekleme()
            else:
                print("Zaten Takiptesiniz")
        except:
            pass
        try:
            takipBt = self.tarayici.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/div[1]/button""")
            if takipBt.text != "":
                takipBt.click()
                self.bekleme()
        except :
            pass
        self.tarayici.get(r"https://www.instagram.com")   

    def takibiBirak(self,profileName):
        self.tarayici.get(r"https://www.instagram.com/{0}".format(profileName))
        try:
            takipBt = self.tarayici.find_element_by_css_selector("button._5f5mN:nth-child(1)")
            if takipBt.text == "":
                takipBt.click()
                self.bekleme()
                birakbt = self.tarayici.find_element_by_css_selector("button.aOOlW:nth-child(1)")
                birakbt.click()
                self.bekleme()
        except:
            pass
        try:
            takipBt = self.tarayici.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/div[1]/button""")
            if takipBt.text != "":
                takipBt.click()
                self.bekleme()
                birakbt = self.tarayici.find_element_by_css_selector("button.aOOlW:nth-child(1)")
                birakbt.click()
                self.bekleme()
        except :
            pass
        self.tarayici.get(r"https://www.instagram.com")

    def listeAl(self,profileName):
        liste = []
        self.tarayici.get(r"https://www.instagram.com/{0}".format(profileName))
        listeBt = self.tarayici.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        self.bekleme()
        pencere = self.tarayici.find_element_by_css_selector("div[role=dialog] ul")
        takipciCount = len(pencere.find_elements_by_css_selector("li"))

        action = webdriver.ActionChains(self.tarayici)

        while True:
            pencere.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            self.bekleme()

            yeniSayi = len(pencere.find_elements_by_css_selector("li"))
            if takipciCount != yeniSayi:
                takipciCount = yeniSayi
                print("yeni gelen",takipciCount)
                self.bekleme()
                if 40<takipciCount<70:
                    for item in pencere.find_elements_by_css_selector("li"):
                        adres = item.find_element_by_css_selector("a").get_attribute("href")
                        liste.append(adres)
                    break
            else:
                break
        for item in liste:
            self.takip(item,mod=1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

