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
#not: Excel dosyalar SQL verileri çekebilir. Dolayısyla verileri değişebilir. 

df = pd.read_excel("Sinan\proje3\TEST_EXCEL_short.xlsx")


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.df = pd.read_excel("Sinan\proje3\TEST_EXCEL_short.xlsx")

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

        #beş parça kutucuktan oluşan ikinci kutucuk ilk etapta Customername,Customer,Salesrep,Productcode ve Productname göstermektedir. 
        #Excel deki C Kolon
        caribilgi = self.win.caribilgi.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].Customername))
        #Excel deki B Kolon
        caribilgi_2 = self.win.caribilgi_2.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].Customer_no))
        #Excel deki D Kolon
        caribilgi_4 = self.win.caribilgi_4.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].salesrep))
        #Excel deki E Kolon
        caribilgi_3 = self.win.caribilgi_3.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].productcode))
        #Excel deki F Kolon
        caribilgi_5 = self.win.caribilgi_5.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].productname))
        #Excel deki F Kolon
        caribilgi_6 = self.win.caribilgi_6.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].Amount))
        #Excel deki F Kolon
        caribilgi_7 = self.win.caribilgi_7.setText(str(self.df[self.df.ORDNERNO==int(siparisno)].loc[0].Price))
        if not True:

            print("Böyle bir siparişno yok")      

#temizle butonun fonksiyonu

    def temizle(self):
        self.win.carikodugiris.setText(" ")
        self.win.caribilgi.setText(" ")
        self.win.caribilgi_2.setText(" ")
        self.win.caribilgi_3.setText(" ")
        self.win.caribilgi_4.setText(" ")
        self.win.caribilgi_5.setText(" ") 
        
        self.win.caribilgi_6.setText(" ")
        self.win.caribilgi_7.setText(" ")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



    #def otomatik(self):
    #    self.win.txtUserInput.setText(#"buraya kullanıcıadınızı giriniz")
    #    self.win.txtSifre.setText(#"buraya şifrenizi giriniz")