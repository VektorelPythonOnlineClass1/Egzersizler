from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("İlk arayüz")
pencere.geometry("300x300+200+200")

def tikla():
    messagebox.showwarning("Kırmızı çizgi", "Hocanın görüntüsü kapanmaz")


dugme = Button(pencere,text="Tıkla",command=tikla)
dugme.grid(column=0,row=0)
    
pencere.mainloop()