from django.urls import path
from rest_framework import routers

from .views import (
    FarmerViewSet,
    TillageViewSet,
    CommunicationViewSet,
)


router = routers.DefaultRouter()

router.register(
    'farmers',
    FarmerViewSet,
    basename='farmers',
)

router.register(
    'tillages',
    TillageViewSet,
    basename='tillages',
)

router.register(
    'communications',
    CommunicationViewSet,
    basename='communications',
)

urlpatterns = []

urlpatterns += router.urls
