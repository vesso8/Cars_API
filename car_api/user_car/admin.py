from django.contrib import admin

from car_api.user_car.models import UserCar


@admin.register(UserCar)
class UserCarAdmin(admin.ModelAdmin):
    list_display = ('user', 'car_brand', 'car_model', 'first_reg', 'odometer')


