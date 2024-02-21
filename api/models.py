from django.db import models 
import datetime
from django.contrib.auth.models import AbstractUser
import django_filters
# Create your models here.



class Person(models.Model):
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 200)
    foto = models.ImageField(null=True, blank=True, upload_to='fotos/')
    class Meta:
        abstract = True

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.CharField(max_length=1000, default=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    productoName = models.CharField(max_length=200)
    productoDescription = models.CharField(blank=True, max_length=500)
    productoPrice = models.DecimalField(max_digits=10, decimal_places=0, default=True)
    productoImage = models.CharField(max_length=10000 ,default=True)
    productoCantidad = models.DecimalField(max_digits=10, decimal_places=0) 
    productoCategoria = models.ManyToManyField(Categorias)
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.productoName
    
class ProductoPopular(models.Model):
    productoName = models.CharField(max_length=200)
    productoImagen = models.CharField(max_length=10000, default=True)
    productoPrice = models.DecimalField(max_digits=10, decimal_places=0, default=True)


def __str__(self):
        return f"Popular: {self.productoName}"


class Carrito(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200, default=True)
    preciounitario = models.DecimalField(max_digits=10, decimal_places=0)
    cantidad = models.DecimalField(max_digits=10, decimal_places=0) 
    subtotal = models.DecimalField(max_digits=10, decimal_places=0, editable=False)

    def total(self):
        return sum(carrito.subtotal for carrito in Carrito.objects.all())

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.preciounitario
        super().save(*args, **kwargs)

    
    def _str_(self):
        return self.nombre

class Jefe(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)



class Comercializadora(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    cantidad = models.DecimalField(max_digits=10, decimal_places=0)
    precio = models.DecimalField(max_digits=10, decimal_places=0)

class Factura(models.Model):
    usuario = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    preciounitario = models.DecimalField(max_digits=10, decimal_places=0)
    cantidad = models.DecimalField(max_digits=10, decimal_places=0) 
    subtotal = models.DecimalField(max_digits=10, decimal_places=0, editable=False)




