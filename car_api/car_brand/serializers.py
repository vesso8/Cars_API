from rest_framework import serializers

from car_api.car_brand.models import CarBrand


class CarBrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id','name')


class CarBrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'name')
