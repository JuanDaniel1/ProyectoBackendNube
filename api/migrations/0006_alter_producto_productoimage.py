# Generated by Django 4.2.7 on 2024-02-20 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_producto_productoimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='productoImage',
            field=models.CharField(default=True, max_length=10000),
        ),
    ]
