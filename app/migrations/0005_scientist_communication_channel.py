# Generated by Django 2.2.2 on 2019-08-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190720_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='communication_channel',
            field=models.CharField(choices=[('whatsapp', 'Grupo de Whatsapp'), ('slack', 'Espacio de Trabajo en Slack'), ('telegram', 'Grupo de Telegram'), ('lista_correo', 'Lista de Correo')], default='', max_length=100),
        ),
    ]