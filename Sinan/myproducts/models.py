from django.db import models
from datetime import datetime
# Create your models here.

class products(models.Model):
    regnumber= models.IntegerField(blank=False)
    product = models.CharField(max_length=100)
    comment = models.TextField(max_length=100,blank=True)
    favorite_lenses = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product