from django.urls import path

from .views import FarmerViewSet, TillageViewSet, LossCommunicationViewSet


urlpatterns = [
	path('farmers/', FarmerViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='farmers'),

    path('tillages/', TillageViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='tillages'),

    path('loss-communications/', LossCommunicationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='loss-communications'),
]
