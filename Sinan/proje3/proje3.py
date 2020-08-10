from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys

import time
import pandas as pd
import numpy as np
import itertools

from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo 
import xlrd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#excel dosya
df = pd.read_excel("Sinan\proje3\TEST_EXCEL.xlsx")


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.df = pd.read_excel("Sinan\proje3\TEST_EXCEL.xlsx")
#pyqt5 designer dosya
#arama buton ve temizle butonun tanımlanması
    def initUI(self):
        self.win = uic.loadUi(r"Sinan\proje3\anasayfa.ui")
        self.win.btngonder.clicked.connect(self.ara)
        self.win.btnsifirla.clicked.connect(self.temizle)
        self.win.show()
#kullanıcıdan gelecek olan 
#ara butonun fonksiyonu
    def ara(self,caribilgi):
        global siparisno
        #kullanıcıdan orderno giris yapılması
        siparisno = self.win.carikodugiris.text()
        #ikinci kutucukta ilk etapta Customer_no, daha sonra Product Name ve Date verilmesini 
        caribilgi = self.win.caribilgi.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].ORDNERNO))
        if not True:
            print("Böyle bir siparişno yok")      
#temizle butonun fonksiyonu
    def temizle(self):
        self.win.carikodugiris.text("")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    #def otomatik(self):
    #    self.win.txtUserInput.setText(#"buraya kullanıcıadınızı giriniz")
    #    self.win.txtSifre.setText(#"buraya şifrenizi giriniz")