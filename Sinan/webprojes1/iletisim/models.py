from django.db import models
from django.utils import timezone
# Create your models here.
class iletisimModel(models.Model):
    adi = models.CharField(max_length=100)
    soyadi = models.CharField(max_length=100)
    telefon= models.CharField(max_length=10)
    eposta = models.EmailField()
    konu = models.TextField()
    aciklama= models.TextField()
    gonderi_tar = models.DateTimeField(default=timezone.now)
    okunma_tar = models.DateTimeField(blank=True,null=True)

    def okundu(self):
        self.okunma_tar = timezone.now()
        self.save()

    def __str__(self):
        liste = [self.adi,self.soyadi,self.telefon,self.konu]
        return ' '.join(liste)
