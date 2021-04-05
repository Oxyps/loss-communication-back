from rest_framework import serializers

from .models import Farmer, Tillage, Communication
from .choices import LOSS_CAUSES


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class TillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tillage
        fields = '__all__'

class CommunicationReadSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer(required=False, read_only=True)
    tillage = TillageSerializer(required=False, read_only=True)

    class Meta:
        model = Communication
        fields = '__all__'

class CommunicationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'
