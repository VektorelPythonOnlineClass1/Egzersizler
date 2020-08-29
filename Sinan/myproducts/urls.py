from django.urls import path, include
from myproducts import views
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import url
from django.urls import reverse_lazy
from django.views import generic

urlpatterns = [
    path('about/',views.about,name="about"),
    path('index/',views.index,name="index"),
    path('',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('delete/<products_id>',views.delete,name="delete"),
]