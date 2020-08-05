from django.shortcuts import render

def iletisimListele(request):
    return render(request,'iletisim/iletisimListe.html',{})