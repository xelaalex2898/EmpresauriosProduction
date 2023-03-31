from django import forms
from .models import Providers, ConvenienceStore 


class ProvidersForm(forms.ModelForm):
    name=forms.CharField(max_length=30,label="Nombre")
    location=forms.CharField(max_length=100,label="Ubicación")
    telephone=forms.CharField(max_length=12,label="Teléfono")
    descripcion=forms.TextField(label="Descripción")
    class Meta:
        model = Providers
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
    descripcion=forms.TextField(label="Descripción")
    class Meta:
        model = ConvenienceStore
        fields = (
            "name",
            "location",
            "telephone",
            "descripcion",
        )    
