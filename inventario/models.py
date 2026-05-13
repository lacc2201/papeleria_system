from django.db import models
from decimal import Decimal


class Categoria(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=200)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    cantidad = models.IntegerField(default=0)

    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    # COSTO APROXIMADO
    def precio_compra(self):
        return self.precio_venta * Decimal('0.80')

    # GANANCIA
    def ganancia(self):
        return self.precio_venta * Decimal('0.20')

    def stock_bajo(self):
        return self.cantidad <= 5

    def __str__(self):
        return self.nombre


class Venta(models.Model):

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    cantidad = models.IntegerField()

    fecha = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.producto.precio_venta * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"