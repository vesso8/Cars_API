from rest_framework import serializers

from car_api.car_model.models import CarModel


class CarModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('car_brand', 'name')

class CarModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('car_brand', 'name')

