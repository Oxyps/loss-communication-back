from django.contrib import admin

from loss_communication.models import Farmer, Tillage, LossCommunication

admin.site.register([Farmer, Tillage, LossCommunication])
