from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("ilk arayüz")
pencere.geometry("300x300+200+200")
def tikla():
    messagebox.showwarning("Kırmızı Çizgi","Kamera kapatılmasın")
    deneme = StringVar()
    deneme.set("tıklandı")
    yazi.delete(0,"end")
    yazi.insert(0,"tıklandı")


dugme = Button(pencere,text="Tıkla",command=tikla,height=5,width=5)
dugme.grid(column=0,row=0)
etiket = Label(text="deneme")
etiket.grid(column=1,row=0)
yazi = Entry(pencere,width=10)
yazi.grid(column=0,row=1)
pencere.mainloop()
