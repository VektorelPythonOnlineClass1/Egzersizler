from tkinter import *

pencere = Tk()
pencere.title("Uyarı")
pencere.geometry("550x315+350+50")

pencere.wm_attributes("-alpha", 0.900)
yazı = Label(text = "dünya",height = 5 ,fg = "red", bg = "black", pady = 20,padx = 50, justify = "left", anchor = "se")

def masaj():
    print("slm")
def degistir():
    etiket["text"] = "merhaba dünya"
etiket = Label (text = "hello world")
def kapat():
    quit()

def verileri_al ():
    etiket["text"] = yazi.get()


etiket.pack()
buton = Button(text = "tıkla bakalım", command = degistir)
buton2 = Button (text = "Kapat" , command = kapat)
buton3 = Button(text = "verileri al", command = verileri_al)
yazi = Entry()
yazi.pack()







yazı.pack()
buton.pack()
buton2.pack()
buton3.pack()
mainloop()

