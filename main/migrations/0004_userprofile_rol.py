# Generated by Django 5.0.6 on 2024-07-19 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_comuna_cod_inmueble_comuna_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rol',
            field=models.CharField(choices=[('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario'), ('admin', 'Admin')], default='arrendador', max_length=255),
        ),
    ]
