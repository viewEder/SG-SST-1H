# Generated by Django 3.2.6 on 2021-11-12 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20211112_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='docscomite',
            name='tipo_documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='documentos.tipodocumento'),
        ),
        migrations.AddField(
            model_name='docuempleados',
            name='tipo_documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='documentos.tipodocumento'),
        ),
        migrations.AddField(
            model_name='docuempresa',
            name='tipo_documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='documentos.tipodocumento'),
        ),
    ]
