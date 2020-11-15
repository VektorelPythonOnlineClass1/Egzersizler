from django.shortcuts import render
from  .models import iletisimModel

def iletisimListele(request):
    mesajlar = iletisimModel.objects.all()
    return render(request,'iletisim/iletisimListe.html',{})