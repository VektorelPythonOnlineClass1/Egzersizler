from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name="about"),
    path('index/',views.index,name="index"),
    path('',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('delete/<products_id>',views.delete,name="delete"),
    
]
