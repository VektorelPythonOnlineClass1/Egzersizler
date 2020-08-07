from django.db import models
from django.utils import timezone

# Create your models here.
class iletisimModel(models.Model):
    adi = models.CharField(max_length=100, verbose_name="Adı")
    soyadi = models.CharField(max_length=100, verbose_name="Soyadı")
    telefon = models.CharField(max_length=10, verbose_name="Telefon")
    eposta = models.EmailField(verbose_name="E-Posta")
    konu = models.TextField(verbose_name="Konu")
    aciklama = models.TextField(verbose_name="Açıklama")
    gonderi_tar = models.DateTimeField(default=timezone.now, verbose_name="Gönderi Tarihi")
    okunma_tar = models.DateTimeField(blank=True, null=True, verbose_name="Okunma Tarihi")

    def okundu(self):
        self.okunma_tar = timezone.now()
        self.save()

    def __str__(self):
        liste = [self.adi, self.soyadi, self.telefon, self.konu]
        return ' '.join(liste)
