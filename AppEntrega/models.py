from django.db import models

# Create your models here.
class ProductoModel(models.Model):
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    codigo=models.IntegerField()
    descripcion=models.TextField()
    class Meta:
        db_table="Producto" 
    def __str__(self):
        return f"Nombre: {self.nombre}'\n' Color: {self.color} Tipo: {self.tipo} Codigo: {self.codigo} Descripcion: {self.descripcion}" 
  

class ClienteModel(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField()
    documento=models.IntegerField()
    class Meta:
        db_table="Cliente"     
    def __str__(self):
        return f"Nombre:{self.nombre} Email:{self.email} Documento:{self.documento}" 

class TiendaModel(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    telefono=models.IntegerField()
    class Meta:
        db_table="Tienda"   
    def __str__(self):
        return f"Nombre: {self.nombre} Direccion: {self.direccion} Telefono: {self.telefono}"   

