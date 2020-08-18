from django import forms
from .models import products

class ListForm(forms.ModelForm):
    class Meta:
        model = products
        fields = {"regnumber","product","comment","favorite_lenses","date"}
        