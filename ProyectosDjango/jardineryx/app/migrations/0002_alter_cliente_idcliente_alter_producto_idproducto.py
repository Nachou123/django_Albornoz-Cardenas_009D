# Generated by Django 4.0.5 on 2022-06-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Id del cliente'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Id del producto'),
        ),
    ]
