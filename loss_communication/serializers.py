from rest_framework import serializers

from .models import Farmer, Tillage, LossCommunication


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class TillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tillage
        fields = '__all__'

class LossCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LossCommunication
        fields = '__all__'
