from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"myproducts/index.html")
def about(request):
    return render(request,"myproducts/about.html")