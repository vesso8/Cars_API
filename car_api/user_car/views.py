from rest_framework import generics as api_views

from car_api.user_car.models import UserCar
from car_api.user_car.serializers import UserCarListSerializer, UserCarCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class UserCarCreateView(api_views.CreateAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class UserCarListView(api_views.ListAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = (
        'car_brand',
        'car_model',
    )
    search_fields = (
        '^odometer',
    )
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class UserCarDetailsView(api_views.RetrieveUpdateAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarCreateSerializer