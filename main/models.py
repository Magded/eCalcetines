from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.timezone import now as timezone_now
import os

def upload_image(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    time_stamp = now.strftime("%d%H%M%S")
    pk = str(getattr(instance, "pk"))
    return "product_image/%s_%s%s" % (pk, time_stamp, filename_ext.lower())


# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=32, verbose_name='Nombre')
    imagen = models.ImageField(upload_to=upload_image, null=True, blank=True)
    precio = models.FloatField()
    cantidad_en_bodega = models.PositiveSmallIntegerField()
    codigo = models.IntegerField(null=True, blank=True)
    oferta = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    estado_choice = [
        ('EN PROCESO', 'EN PROCESO'),
        ('ENTREGADO', 'ENTREGADO'),
        ('PAGADO', 'PAGADO'),
    ]
    producto = models.ForeignKey(Producto, on_delete=SET_NULL,  null=True)
    estado = models.TextField(choices=estado_choice)
    usuario = models.TextField()
    cantidad = models.IntegerField()
    delivery_type = models.TextField()
