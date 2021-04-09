from django.contrib.gis.measure import Distance
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

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

	filter_backends = [DjangoFilterBackend, SearchFilter]
	filterset_fields = ['id', 'name', 'cpf', 'email']
	search_fields = ['id', 'name', 'cpf', 'email']


class TillageViewSet(
	ReadWriteSerializerMixin,
	viewsets.ModelViewSet,
):
	queryset = Tillage.objects.all().order_by('id')
	read_serializer_class = TillageReadSerializer
	write_serializer_class = TillageWriteSerializer

	filter_backends = [DjangoFilterBackend, SearchFilter]
	filterset_fields = ['id', 'type', 'harvest_date']
	search_fields = ['id', 'type', 'harvest_date']


class CommunicationViewSet(
	ReadWriteSerializerMixin,
	viewsets.ModelViewSet,
):
	queryset = Communication.objects.all().filter(is_dirty=False).order_by('id')
	read_serializer_class = CommunicationReadSerializer
	write_serializer_class = CommunicationWriteSerializer

	filter_backends = [DjangoFilterBackend, SearchFilter]
	filterset_fields = ['id', 'loss_cause', 'farmer__cpf', 'is_dirty']
	search_fields = ['id', 'loss_cause', 'farmer__cpf']

	def create(self, request):
        response_status = None

		if tillageLocationAlreadyExists(
			request.data.get('tillage')
		):
			request.data['is_dirty'] = True
            response_status = status.HTTP_200_OK
			print(request.data)
		else:
			request.data['is_dirty'] = False
            response_status = status.HTTP_201_OK

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)

		return Response(
			serializer.data,
			status=response_status,
			headers=headers
		)
