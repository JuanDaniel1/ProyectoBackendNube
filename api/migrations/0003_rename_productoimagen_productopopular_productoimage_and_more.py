# Generated by Django 4.2.7 on 2024-02-13 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_mundo_producto_productocategoria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productopopular',
            old_name='productoImagen',
            new_name='productoImage',
        ),
        migrations.AddField(
            model_name='productopopular',
            name='productoCantidad',
            field=models.DecimalField(decimal_places=0, default=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='productopopular',
            name='productoCategoria',
            field=models.ManyToManyField(to='api.categorias'),
        ),
        migrations.AddField(
            model_name='productopopular',
            name='productoDescription',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]