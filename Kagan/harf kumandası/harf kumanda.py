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
        self.win = uic.loadUi(r"C:\Users\kagan\OneDrive\Masaüstü\python kurs\visual sutudio\Egzersizler\Kagan\deneme.deneme/kumanda.ui")
        self.win.btGiris.clicked.connect(self.giris) 
        self.win.show()


    def giris(self):
        harf = self.win.harf.text()
        self.kumanda = HarfKumanda()
        self.kumanda.girisYap()    

    

class HarfKumanda:
    def __init__(self,harf):
        self.harf = harf



    def HarfGir(self):
        if harf ==1:
            a = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["a"])
            print(a)
            if harf ==2:
                b = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["b"])
                print(b)
                if harf ==3:
                    c = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["c"])
                    print(c)
                    if harf ==4:
                        d = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["d"])
                        print(d)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())                   