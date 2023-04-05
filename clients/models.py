from django.db import models

class Providers:
    name=models.CharField(default="",max_length=30,verbose_name="Nombre")
    location=models.CharField(max_length=100,verbose_name="Ubicación")
    telephone=models.CharField(default="",max_length=12,verbose_name="Teléfono")
    descripcion=models.TextField(default="",verbose_name="Descripción")

    class Meta:
        verbose_name_plural="Proveedores"
    def __str__(self) -> str:
        return "%s"%(self.name)
class ConvenienceStore:
    name=models.CharField(default="",max_length=30,verbose_name="Nombre")
    location=models.CharField(max_length=100,verbose_name="Ubicación")
    telephone=models.CharField(default="",max_length=12,verbose_name="Teléfono")
    descripcion=models.TextField(default="",verbose_name="Descripción")
    class Meta:
        verbose_name_plural="Tiendas minoristas"
    def __str__(self) -> str:
        return "%s"%(self.name)
    

