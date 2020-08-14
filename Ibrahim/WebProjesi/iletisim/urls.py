from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.iletisimListele,name="iletisimListele"),
    path('detay/<int:pk>',views.iletisimDetay,name='iletisimDetay'),
    path('yeni/',views.yeniMesaj,name="yeniMesaj"),
    path('duzenle/<int:pk>',views.iletisimDuzenle,name="iletisimDuzenle"),
]
