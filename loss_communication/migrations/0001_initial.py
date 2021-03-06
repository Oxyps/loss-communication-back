# Generated by Django 3.1.7 on 2021-04-04 04:13

import cpf_field.models
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'farmer',
            },
        ),
        migrations.CreateModel(
            name='Tillage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('type', models.CharField(max_length=255)),
                ('harvest_date', models.DateField()),
            ],
            options={
                'db_table': 'tillage',
            },
        ),
        migrations.CreateModel(
            name='LossCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loss_cause', models.CharField(choices=[('EXCESSIVE_RAIN', 'Chuva excessiva'), ('FROST', 'Geada'), ('FROZEN_RAIN', 'Granizo'), ('DRY', 'Seca'), ('GALE', 'Vendaval'), ('THUNDER', 'Raio')], max_length=255)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_communication.farmer')),
                ('tillage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loss_communication.tillage')),
            ],
            options={
                'db_table': 'loss_communication',
            },
        ),
    ]
