# Generated by Django 3.2.6 on 2021-11-05 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0005_auto_20211025_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_Emergencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacto_emergencia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto Emergencia')),
                ('parentesco_emergercia', models.CharField(blank=True, choices=[('Padres', 'Padres'), ('Hermanos', 'Hermanos'), ('Conyugue', 'Conyugue'), ('Hijos', 'Hijos'), ('Otro', 'Otro')], max_length=20, null=True, verbose_name='Parentesco')),
                ('telefono_emergencia', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono Emergencia')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario__username'],
            },
        ),
    ]