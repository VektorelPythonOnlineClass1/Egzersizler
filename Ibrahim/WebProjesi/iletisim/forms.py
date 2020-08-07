from django import forms 
from .models import iletisimModel

class iletisimForm(forms.models.ModelForm):
    class Meta:
        model =iletisimModel
        fields = ("adi","soyadi","telefon","eposta","konu","aciklama",)