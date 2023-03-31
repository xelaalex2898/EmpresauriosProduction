from django.db import models

class Clients:
    name=models.CharField(default="",max_length=30,verbose_name="Nombre")
    telephone=models.CharField(default="",max_length=12,verbose_name="Teléfono")
    direction=models.CharField(default="",max_length=100, verbose_name="Dirección")
    is_provider=models.BooleanField(default=False, verbose_name="Es proveedor")
    provider=models.ForeignKey(ConvenienceStore,on_delete=models.CASCADE,verbose_name="ID proveedor")
    class Meta:
        verbose_name_plural="Catálogo"
    def __str__(self) -> str:
        return "%s"%(self.product)
class ConvenienceStore:
    
    location=models.CharField(max_length=100,)

