from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics as api_views
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from car_api.car_brand.models import CarBrand
from car_api.car_brand.serializers import CarBrandListSerializer, CarBrandCreateSerializer


class CarBrandCreateView(api_views.CreateAPIView):
    queryset = CarBrand.objects.all()
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = (
    #     'name',
    # )
    #
    # search_fields = (
    #     ('^name',)
    # )
    serializer_class = CarBrandCreateSerializer
    # list_serializer_class = CarBrandListSerializer
    # create_serializer_class = CarBrandCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

    # def get_serializer_class(self):
    #     if self.request.method.lower() == 'post':
    #         return self.create_serializer_class
    #     return self.list_serializer_class

class CarBrandListView(api_views.ListAPIView):
    queryset = CarBrand.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = (
        'name',
    )

    search_fields = (
        ('^name',)
    )
    serializer_class = CarBrandListSerializer
    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

class CarBrandDetailsView(api_views.RetrieveUpdateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandCreateSerializer


