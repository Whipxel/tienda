from django.db.models import IntegerField, ImageField, FloatField, CharField, ForeignKey, CASCADE, Model
from django.contrib.auth import get_user_model


# Create your models here.
class CarritoCompras(Model):
    FK_UsuarioCliente = ForeignKey(get_user_model(), on_delete=CASCADE)

    class Meta:
        db_table = 'CarritoCompras'


class CategoriaProducto(Model):
    Nombre = CharField(max_length=100)
    Descripcion = CharField(max_length=200)

    class Meta:
        db_table = 'CategoriaProducto'


class Producto(Model):
    Nombre = CharField(max_length=150)
    Precio = FloatField(default=0.0)
    Descripcion = CharField(max_length=200)
    Imagen = ImageField(upload_to='imagenes_productos_inventario')
    Stock = FloatField(default=0.0)
    FK_Categoria = ForeignKey(CategoriaProducto, on_delete=CASCADE)

    class Meta:
        db_table = 'Producto'


class CarritoTieneProductos(Model):
    FK_Producto = ForeignKey(Producto, on_delete=CASCADE)
    FK_Carrito = ForeignKey(CarritoCompras, on_delete=CASCADE)
    Cantidad = IntegerField(default=1)

    class Meta:
        db_table = 'CarritoTieneProductos'


class TiposDeEnvio(Model):
    Nombre = CharField(max_length=150)
    Clasificacion = CharField(max_length=150)
    Descripcion = CharField(max_length=200)

    class Meta:
        db_table = 'TiposDeEnvio'


class HistorialCompras(Model):
    FK_UsuarioCliente = ForeignKey(get_user_model(), on_delete=CASCADE)
    NumeroDeOrden = CharField(max_length=100)
    TipoEnvio = CharField(max_length=100)

    class Meta:
        db_table = 'HistorialCompras'


class ProductoComprado(Model):
    Cantidad = IntegerField(default=1)
    Nombre = CharField(max_length=150)
    Precio = FloatField(default=0.0)
    Descripcion = CharField(max_length=200)
    Imagen = ImageField(upload_to='imaenges_productos_comprados')
    FK_HistorialCompras = ForeignKey(HistorialCompras, on_delete=CASCADE)

    class Meta:
        db_table = 'ProductoComprado'
