from rest_framework import viewsets, status
from django.contrib.gis.measure import Distance
from rest_framework.response import Response

from .serializers import (
    FarmerSerializer,
    TillageReadSerializer,
    TillageWriteSerializer,
    CommunicationReadSerializer,
    CommunicationWriteSerializer,
)
from .models import Farmer, Tillage, Communication
from .mixins import ReadWriteSerializerMixin


def tillageLocationAlreadyExists(tillage_id):
    tillage = Tillage.objects.filter(id=tillage_id).values()[0]

    existing_near_tillages = Tillage.objects.filter(
        # location__distance_lt=(tillage['location'], Distance(km=10))
        location__distance_lt=(tillage['location'], 10)
    ).values()

    return len(existing_near_tillages) > 1


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all().order_by('id')
    serializer_class = FarmerSerializer

class TillageViewSet(
    ReadWriteSerializerMixin,
    viewsets.ModelViewSet,
):
    queryset = Tillage.objects.all().order_by('id')
    read_serializer_class = TillageReadSerializer
    write_serializer_class = TillageWriteSerializer

class CommunicationViewSet(
    ReadWriteSerializerMixin,
    viewsets.ModelViewSet,
):
    queryset = Communication.objects.all().order_by('id')
    read_serializer_class = CommunicationReadSerializer
    write_serializer_class = CommunicationWriteSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if tillageLocationAlreadyExists(
            serializer.validated_data.get('tillage').id
        ):
            return Response(
                {'message': 'This tillage location may already exists.'},
                status=status.HTTP_409_CONFLICT,
            )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
