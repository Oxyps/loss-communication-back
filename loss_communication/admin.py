from django.contrib import admin

from loss_communication.models import Farmer, Tillage, Communication

admin.site.register([Farmer, Tillage, Communication])
