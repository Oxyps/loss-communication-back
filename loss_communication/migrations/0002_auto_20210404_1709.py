# Generated by Django 3.1.7 on 2021-04-04 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loss_communication', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LossCommunication',
            new_name='Communication',
        ),
        migrations.AlterModelTable(
            name='communication',
            table='communication',
        ),
    ]
