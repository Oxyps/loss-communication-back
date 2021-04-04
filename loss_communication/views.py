from rest_framework import viewsets

from .serializers import FarmerSerializer, TillageSerializer, LossCommunicationSerializer
from .models import Farmer, Tillage, LossCommunication


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all().order_by('name')
    serializer_class = FarmerSerializer

class TillageViewSet(viewsets.ModelViewSet):
    queryset = Tillage.objects.all().order_by('type')
    serializer_class = TillageSerializer

class LossCommunicationViewSet(viewsets.ModelViewSet):
    queryset = LossCommunication.objects.all().order_by('loss_cause')
    serializer_class = LossCommunicationSerializer
