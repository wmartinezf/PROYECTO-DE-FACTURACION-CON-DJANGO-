# Generated by Django 3.0.8 on 2020-08-08 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Proyecto_ORM', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='creacion',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='modificacion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='creacion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='modificacion',
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(default=datetime.date(2020, 8, 8), verbose_name='Fecha'),
        ),
    ]