# Generated by Django 3.2.7 on 2021-09-30 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0002_alter_destino_nombre'),
        ('usuarios', '0001_initial'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reserva',
            unique_together={('viaje', 'usuario')},
        ),
    ]
