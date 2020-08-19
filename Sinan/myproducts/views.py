from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products
from .forms import ListForm

def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            myproducts=products.objects.all()
            return render(request,"myproducts/index.html",{"myproducts":myproducts})
    else:
        myproducts=products.objects.all()
        return render(request,"myproducts/index.html",{"myproducts":myproducts})
def about(request):
    return render(request,"myproducts/about.html")

def create(request):
    if request.method == "POST":
        form = ListForm (request.POST or None)
        if form.is_valid:
            form.save()
            myproducts=products.objects.all()
            return render(request,"myproducts/create.html",{"myproducts":myproducts})
    else:
        myproducts=products.objects.all()
        return render(request,"myproducts/create.html",{"myproducts":myproducts})

def delete(request,products_id):
    product = products.objects.get(pk=products_id)
    product.delete()
    return redirect("index")

