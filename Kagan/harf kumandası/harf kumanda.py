from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.win = uic.loadUi(r"C:\Users\kagan\OneDrive\Masaüstü\python kurs\visual sutudio\Egzersizler\Kagan\harf kumandası/kumanda.ui")
        self.win.btGiris.clicked.connect(self.giris)
        self.win.btIptal.clicked.connect(self.temizle)
        self.win.show()


    def giris(self):
        harf = self.win.harf.text()
        self.HarfKumanda = HarfKumanda(harf)
        self.HarfKumanda.girisYap()


    def temizle(self):
        self.win.harf.setText("")        



class HarfKumanda:
    def __init__(self,harf):
        self.harf = harf
  


    def girisYap(self):
        if self.harf ==1:
            a = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["a"])
            print(a)
            if self.harf ==2:
                b = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["b"])
                print(b)
                if self.harf ==3:
                    c = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["c"])
                    print(c)
                    if self.harf ==4:
                        ç = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["ç"])
                        print(ç)
                        if self.harf ==5:
                            d = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["d"])
                            print(d)
                            if self.harf ==6:
                                e = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["e"])
                                print(e)
                                if self.harf ==7:
                                    f = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["fe"])
                                    print(f)
                                    if self.harf ==8:
                                        g = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["g"])
                                        print(g)
                                        if self.harf ==9:
                                            ğ = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["ğ"])
                                            print(ğ)
                                            if self.harf ==10:
                                                h = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["h"])
                                                print(h)
                                                if self.harf ==11:
                                                    i = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["i"])
                                                    print(i)
                                                    if self.harf ==12:
                                                        ı = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["ı"])
                                                        print(ı)
                                                        if self.harf ==13:
                                                            j = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["j"])
                                                            print(j)
                                                            if self.harf ==14:
                                                                k = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["k"])
                                                                print(k)
                                                                if self.harf ==15:
                                                                    l = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["l"])
                                                                    print(l)
                                                                    if self.harf ==16:
                                                                        m = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["m"])
                                                                        print(m)
                                                                        if self.harf ==17:
                                                                            n = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["n"])
                                                                            print(n)
                                                                            if self.harf ==18:
                                                                                o = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["o"])
                                                                                print(o)
                                                                                if self.harf ==19:
                                                                                    ö = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["ö"])
                                                                                    print(ö)
                                                                                    if self.harf ==20:
                                                                                        p = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["p"])
                                                                                        print(p)
                                                                                        if self.harf ==21:
                                                                                            r = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["r"])
                                                                                            print(r)
                                                                                            if self.harf ==22:
                                                                                                s = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["s"])
                                                                                                print(s)
                                                                                                if self.harf ==23:
                                                                                                    ş = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["ş"])
                                                                                                    print(ş)
                                                                                                    if self.harf ==24:
                                                                                                        t = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["t"])
                                                                                                        print(t)
                                                                                                        if self.harf ==25:
                                                                                                            u = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["u"])
                                                                                                            print(u)
                                                                                                            if self.harf ==26:
                                                                                                                ü = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["ü"])
                                                                                                                print(ü)
                                                                                                                if self.harf ==27:
                                                                                                                    v = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["v"])
                                                                                                                    print(v)
                                                                                                                    if self.harf ==28:
                                                                                                                        y = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["y"])
                                                                                                                        print(y)
                                                                                                                        if self.harf ==29:
                                                                                                                            z = pd.DataFrame(np.random.randint(10,size=(0,1)),columns=["z"])
                                                                                                                            print(z),print(lblSonuc)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())                   