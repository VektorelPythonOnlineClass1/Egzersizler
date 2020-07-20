print("Hesap makinesine hoş geldiniz")

print("""***************************** 
Hesap Makinesi Programı

işlemler:

1. Toplama işlemi [+]

2. Çıkarma işlemi [-]

3. Çarpma işlemi  [*]

4. Bölüm işlemi   [/]

*****************************
""")

a= int(input("Birinci Sayı: "))
b= int(input("İkinci Sayı: "))
işlem = input("Lütfen dört işlemden birini seçiniz: ")
if işlem == "1":
    print("{} ile {} sayıların toplamı {} dir".format(a,b,a+b))
elif işlem =="2":
    print("{} ile {} sayıların çıkarması {} dır".format(a, b, a - b))
elif işlem =="3":
    print("{} ile {} sayıların çarpımı {} dır".format(a, b, a * b))
elif işlem =="4":
    print("{} ile {} sayıların bölümün {} dır".format(a, b, a / b))
else:
    print("gerçersiz işlem")