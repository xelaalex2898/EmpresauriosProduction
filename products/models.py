from django.db import models
from clients.models import Providers
class Products:
    #¿solo la tinda tiene el control de su inventario tiene el control de su inventario?? sí
    #opcion 2 la organización tiene acceso al inventario de todas las tiendas
    Name=models.CharField(max_length=20, default="Name", verbose_name="Nombre")
    PricePerMayority=models.FloatField(min=0,default=0, verbose_name="Precio por mayoreo")
    Marca=models.CharField(max_length=20,default="Marca",verbose_name="Marca")
    clasification=models.CharField(max_length=50,default="clasificación",verbose_name="Clasificación")
    #esta es la cantidad disponible en tienda
    quantity=models.FloatField(min=0,default=0,verbose_name="Cantidad Disponible")
    #clave foranea
    provider=models.ForeignKey(Providers,on_delete=models.CASCADE,verbose_name="Proveedor")
    
    class Meta:
        verbose_name_plural="Catálogo"
    def __str__(self) -> str:
        return "El proveedor es: %s, %s"%( self.provider,self.Name)
