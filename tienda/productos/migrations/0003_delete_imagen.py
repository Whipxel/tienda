# Generated by Django 3.0.5 on 2020-06-10 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_comentario_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]