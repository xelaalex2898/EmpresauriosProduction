from django import forms
from .models import Clients, ConvenienceStore 


class ProvidersForm(forms.ModelForm):
    name=forms.CharField(max_length=30,label="Nombre")
    location=forms.CharField(max_length=100,label="Ubicación")
    telephone=forms.CharField(max_length=12,label="Teléfono")
    descripcion=forms.CharField(max_length=100,label="Descripción")
    class Meta:
        model = Clients
        fields = (
            "name",
            "location",
            "telephone",
            "descripcion",
        )
class ConvenienceStoreForm(forms.ModelForm):
    name=forms.CharField(max_length=30,label="Nombre")
    location=forms.CharField(max_length=100,label="Ubicación")
    telephone=forms.CharField(max_length=12,label="Teléfono")
    descripcion=forms.CharField(max_length=100,label="Descripción")
    class Meta:
        model = ConvenienceStore
        fields = (
            "name",
            "location",
            "telephone",
            "descripcion",
        )    