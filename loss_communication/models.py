from django.contrib.gis.db import models
from cpf_field.models import CPFField

from .choices import LOSS_CAUSES

class Farmer(models.Model):
    class Meta:
        db_table = 'farmer'

    cpf = CPFField('cpf', null=False)
    email = models.EmailField(null=False)
    name = models.CharField(null=False, max_length=255)

class Tillage(models.Model):
    class Meta:
        db_table = 'tillage'

    location = models.PointField(null=False)
    type = models.CharField(null=False, max_length=255)
    harvest_date = models.DateField(null=False)

class LossCommunication(models.Model):
    class Meta:
        db_table = 'loss_communication'

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    tillage = models.ForeignKey(Tillage, on_delete=models.CASCADE)
    loss_cause = models.CharField(choices=LOSS_CAUSES, null=False, max_length=255)
