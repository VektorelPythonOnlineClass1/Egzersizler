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


df = pd.read_excel ("D:\Python3\Egzersizler\Sinan\proje3\TEST_EXCEL.xlsx")

agroup = df.groupby (list(df['Customer_no']))
print(agroup.sum())
bgroup = df.groupby (list(df['Customername']))
print(bgroup.sum())
cgroup = df.groupby (list(df['salesrep']))
print(cgroup.sum())
dgroup = df.groupby (list(df['productcode']))
print(dgroup.sum())
egroup = df.groupby (list(df['productname']))
print(egroup.sum())
fgroup = df.groupby (list(df['Amount']))
print(fgroup.sum())
ggroup = df.groupby (list(df['Price']))
print(ggroup.sum())


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"Sinan\proje3\anasayfa.ui")
        self.win.btngonder.clicked.connect(self.ara)
        self.win.btnsifirla.clicked.connect(self.temizle)
        self.win.show()

    def ara(self,caribilgi):
        global carikodu 
        carikodu = self.win.txtcarikodugiris.text()
        caribilgi = self.win.txtcaribilgi.setText()
        i = 0
        if caribilgi == lişt(df['Customer_no'][i][1]):
            return (self.win.txtcaribilgi.setText(lişt(df['Customer_no'][i][1])))
        else:  
            i=+1
        
    def temizle(self):
        self.win.txtcarikodugiris.text("")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

#ilk başta Excel dökümanı deklare edilmektedir. Dosya,Sayfa ve Hücreleri 

    #def otomatik(self):
    #    self.win.txtUserInput.setText(#"buraya kullanıcıadınızı giriniz")
    #    self.win.txtSifre.setText(#"buraya şifrenizi giriniz")
   

#book = xlrd.open_workbook('Egzersizler\Sinan\proje3\TEST_EXCEL.xlsx')
#sheet = book.sheet_by_name('Sheet')
#data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

#Tablo şeklinde oluşturmak için iki for döngü iç içe olması gerekiyor.
#for j in range(sheet.ncols):
#    for i in range(sheet.nrows):
#        #print(data[i][j])
#        #A kolonu getirmedim, çünkü Tarih formatı görünmemektedir. Bu yüzden direk B kolondan H kolona kadar göstermektedir.
#        print(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7])
#
# Yakında devamı gelecek
# Kolonları yukarıdan aşağı bir Liste olarak toplanılırsa üzerinde filtreleme ve toplama yapılabilinir diye düşünüyorum.
# bunun için Range column diye bir fonksiyon var. Bununla ilgili devam gidilebilinir mi?
