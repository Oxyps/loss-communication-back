from django.contrib.gis.db import models
from cpf_field.models import CPFField

from .choices import LOSS_CAUSES

class Farmer(models.Model):
    cpf = CPFField('cpf', null=False, unique=True)
    email = models.EmailField(null=False)
    name = models.CharField(null=False, max_length=255)

    class Meta:
        db_table = 'farmer'

    def __str__(self):
        return self.name;

class Tillage(models.Model):
    location = models.PointField(null=False)
    type = models.CharField(null=False, max_length=255)
    harvest_date = models.DateField(null=False)

    class Meta:
        db_table = 'tillage'

    def __str__(self):
        return f'{self.type} - {self.location}';

class Communication(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.PROTECT)
    tillage = models.ForeignKey(Tillage, on_delete=models.PROTECT)
    loss_cause = models.CharField(choices=LOSS_CAUSES, null=False, max_length=255)
    is_dirty = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'communication'

    def __str__(self):
        return f'{self.farmer} - {self.loss_cause}';
