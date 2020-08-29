from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products
from .forms import ListForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


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

def login(request):
    return render(request,"myproducts/login.html")

@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})