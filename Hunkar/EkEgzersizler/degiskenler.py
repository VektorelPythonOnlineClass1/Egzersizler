sayi = 10 #integer
tc = "1010101010" #string
isim = "Hünkar"
soyisim = "Genç"
telefonNumarasi="05493811994"
floatSayi=10.0
#tc, telefon numarası gibi matematiksel 
#işlem yapılmayacak değişkenler
#string tutulmalıdır!

#string tuttuğum değerleri sayısal
#değere dönüştürmek için:
print(float(tc) + 10)        

#Değişkenin tipini öğrenmek için:
print(type(floatSayi))
print(type(sayi))
print(type(tc))

##STRINGLER

#first string
firstString = "python is awesome!"

#second string
secondString = "PyThOn Is AwEsOme!"

#Bu iki string değer eşit mi?
#String değerlerin tümünü küçük ya da tümünü büyük
#yapıp kontrol sağlayabiliriz.

if(firstString.upper() == secondString.upper()):
    print("Aynı iki değer tanımladınız.")
else:
    print("Farklı iki değer tanımladınız.")