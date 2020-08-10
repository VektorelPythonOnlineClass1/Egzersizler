from django.shortcuts import render,redirect,get_object_or_404
from .models import iletisimModel
from .forms import iletisimForm

def iletisimListele(request):
    mesajlar = iletisimModel.objects.all()
    # şartlı getirme
    mesajlar = iletisimModel.objects.filter(adi="Ali")
    mesajlar = iletisimModel.objects.get(adi="Ali")
    return render(request,'iletisim/iletisimListe.html',{"mesajlar":mesajlar})


def iletisimDetay(request,pk):
    mesaj = iletisimModel.objects.get(pk=pk)
    return render(request,"iletisim/iletisimDetay.html",{"mesaj":mesaj})


def iletisimDuzenle(request,pk):
    mesaj = get_object_or_404(iletisimModel,pk=pk)
    if request.method == "POST":
        form = iletisimForm(request.POST,instance=mesaj)
        if form.is_valid():
            mesaj = form.save(commit=False)
            ################################
            ################################
            mesaj.save()
            return redirect('iletisimDetay',pk=mesaj.pk)
    else:
        form = iletisimForm(instance=mesaj)
    return render(request,"iletisim/yenimesaj.html",{"form":form})

def yeniMesaj(request):
    if request.method == "POST":
        form = iletisimForm(request.POST)
        if form.is_valid():
            mesaj = form.save(commit=False)
            ################################
            ################################
            mesaj.save()
            return redirect('iletisimDetay',pk=mesaj.pk)
    else:
        form = iletisimForm()
    return render(request,"iletisim/yenimesaj.html",{"form":form})