from rest_framework import serializers

from .models import Farmer, Tillage, Communication
from .choices import LOSS_CAUSES


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class TillageReadSerializer(serializers.ModelSerializer):
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()

    class Meta:
        model = Tillage
        exclude = ['location']

    def get_longitude(self, data):
        return data.location.x

    def get_latitude(self, data):
        return data.location.y

class TillageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tillage
        fields = '__all__'

class CommunicationReadSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer(required=False, read_only=True)
    tillage = TillageReadSerializer(required=False, read_only=True)

    class Meta:
        model = Communication
        fields = '__all__'

class CommunicationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'
