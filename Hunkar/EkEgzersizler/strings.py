# -*- coding: utf-8 -*-

#SUBSTRING#
#---------#

message = "Hello World!"
#String bir çağrı dizisidir.
#Bu sebeple mesaj ifadesinin belli bir
#bölümünü seçerek getirebiliriz.
print(message[2]) #l
print(message[2:5]) #llo
print(message[2:]) #llo World!
print(message[:5]) #Hello
print(message[11:12]) #!

newMessage = message[2:5] #atama işlemi

print(newMessage) #llo

#LEN FONKSİYONU#
#---------#
newMessage2 = message[len(message)-1:len(message)] #atama işlemi
print(newMessage2)

#LOWER-UPPER FONKSİYONU#
#---------#
print(message.upper())
print(message.lower())

#REPLACE FONKSİYONU#
#---------#

print(message.replace("Hello","Hi"))
print(message)

#SPLIT/STRIP FONKSİYONU#
#---------#
info = "27 yaşındayım.".strip()
print(info.split())
print(info.split(" "))
print("Yaşı : " + info.split(" ")[0])


#INPUT
#---------#

name = input("Adınız?")

number1 = input("Sayı 1 ?")
number2 = input("Sayı 2 ?")
print(int(number1)+int(number2))
















