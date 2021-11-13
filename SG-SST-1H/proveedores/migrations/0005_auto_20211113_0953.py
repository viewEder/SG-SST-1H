# Generated by Django 3.2.7 on 2021-11-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0004_alter_elementos_activo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleelementos',
            old_name='vida_útil',
            new_name='vida_util',
        ),
        migrations.AlterField(
            model_name='detalleelementos',
            name='activo',
            field=models.BooleanField(default=False, verbose_name='Se encuentra activo?'),
        ),
    ]
