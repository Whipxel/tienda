from django.contrib import admin
from .models import Producto, CarritoCompras

@admin.register(Producto, CarritoCompras)
class AuthorAdmin(admin.ModelAdmin):
    pass
