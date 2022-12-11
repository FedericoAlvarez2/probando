from django import forms
from django.contrib.auth.models import User




class MotoFormulario(forms.Form):

    marca = forms.CharField(max_length=80)
    modelo = forms.CharField(max_length=80)
    kilometros = forms.IntegerField()
    precio = forms.FloatField()
    #foto = forms.ImageField(upload_to="Fotos")