from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return "Producto: {} Precio: $ {}".format(self.nombre, self.precio)

class Comentario(models.Model):
    comentario= models.CharField(max_length=300)
    usuario = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, related_name="producto_comentarios", on_delete=models.CASCADE)

    def __str__(self):
        return "Comentario: {} Usuario: {} Producto: {}".format(self.comentario, self.usuario, self.producto)

class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes_producto')
    producto = models.ForeignKey(Producto, related_name="producto_imagen", on_delete=models.CASCADE)

    def __str__(self):
        return "Titulo: {}".format(self.titulo)

class CarritoCompras(models.Model):
    usuario = models.ForeignKey(get_user_model(), related_name="carrito_usuario", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name="producto_carrito", on_delete=models.CASCADE)
    precio = models.IntegerField()
    direccion = models.CharField(max_length=300)
    datos_payu = models.CharField(max_length=600)
    comprado = models.BooleanField(default=False)
    pendiente = models.BooleanField(default=False)

    def __str__(self):
        return "Usuario: {} Producto: {}".format(self.usuario, self.producto)