from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey, CASCADE, Model


class BaseUser(AbstractUser):
    Nombre = CharField(max_length=150, unique=True)

    def __str__(self):
        return "username: {}".format(self.email)

    class Meta:
        db_table = 'BaseUser'


class DatosGuia(Model):
    Telefono = CharField(max_length=20)
    Direccion = CharField(max_length=200)
    Calle = CharField(max_length=100)
    NumeroPostal = CharField(max_length=50)
    CodigoPostal = CharField(max_length=50)
    Colonia = CharField(max_length=100)
    Ciudad = CharField(max_length=100)
    Estado = CharField(max_length=150)
    Referencia = CharField(max_length=10)
    ContenidoPaquete = CharField(max_length=150)

    class Meta:
        db_table = 'DatosGuia'


class DatosFiscales(Model):
    RFC = CharField(max_length=80)
    RazonSocial = CharField(max_length=150)
    UsoDeCFDI = CharField(max_length=200)
    Direccion = CharField(max_length=200)
    MetodoPago = CharField(max_length=200)

    class Meta:
        db_table = 'DatosFiscales'


class UsuarioCliente(BaseUser):
    FK_DatosFiscales = ForeignKey(DatosFiscales, on_delete=CASCADE)
    FK_DatosGuia = ForeignKey(DatosGuia, on_delete=CASCADE)

    class Meta:
        db_table = 'UsuarioCliente'


