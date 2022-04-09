from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics as api_views
from rest_framework.filters import SearchFilter, OrderingFilter

from car_api.car_model.models import CarModel
from car_api.car_model.serializers import CarModelListSerializer, CarModelCreateSerializer


class CarModelCreateView(api_views.CreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

class CarModelListView(api_views.ListAPIView):
    queryset = CarModel.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    serializer_class = CarModelListSerializer
    filter_fields = (
        'car_brand',
        'name',
    )
    search_fields = (
        '^name',
    )
    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

class CarModelDetailsView(api_views.RetrieveUpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelCreateSerializer