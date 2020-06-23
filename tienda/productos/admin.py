from django.contrib import admin
from .models import Producto, Comentario, Imagen, CarritoCompras

@admin.register(Producto, Comentario, Imagen, CarritoCompras)
class AuthorAdmin(admin.ModelAdmin):
    pass
