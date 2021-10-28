# Generated by Django 3.2.6 on 2021-10-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20211025_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='profile',
            name='modify_at',
            field=models.DateField(auto_now=True, null=True, verbose_name='Actualizado el'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
    ]