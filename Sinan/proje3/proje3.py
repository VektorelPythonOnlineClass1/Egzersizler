from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys

import time
import pandas 
import numpy

from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo 
import xlrd

#ilk başta Excel dökümanı deklare edilmektedir. Dosya,Sayfa ve Hücreleri 
book = xlrd.open_workbook(r'Sinan\proje3\TEST_EXCEL.xlsx')
sheet = book.sheet_by_name('Sheet')
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

#Tablo şeklinde oluşturmak için iki for döngü iç içe olması gerekiyor.
for j in range(sheet.ncols):
    for i in range(sheet.nrows):
        #print(data[i][j])
        #A kolonu getirmedim, çünkü Tarih formatı görünmemektedir. Bu yüzden direk B kolondan H kolona kadar göstermektedir.
        print(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7])

# Yakında devamı gelecek
# Kolonları yukarıdan aşağı bir Liste olarak toplanılırsa üzerinde filtreleme ve toplama yapılabilinir diye düşünüyorum.
# bunun için Range column diye bir fonksiyon var. Bununla ilgili devam gidilebilinir mi?