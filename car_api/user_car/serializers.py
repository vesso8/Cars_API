from rest_framework import serializers

from car_api.user_car.models import UserCar


class UserCarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ('user', 'first_reg', 'odometer')


class UserCarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ('user', 'car_brand', 'car_model', 'first_reg', 'odometer')
