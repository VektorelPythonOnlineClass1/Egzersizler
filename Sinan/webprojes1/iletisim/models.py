from django.db import models
from django.utils import timezone
# Create your models here.
class iletisimModel(models.Model)
    adi = models.CharField(max_length=100)
    soyadi = models.CharField(max_length=100)
    telefon= models.PhoneNumberField()
    eposta = models.EmailField()
    konu = models.TextField()
    aciklama= models.TextField()
    gonderi_tar= models.DateTimeField(default-timezone.now)
    okuma_tar = models.DateTimeField(blank= True, mail=True)

