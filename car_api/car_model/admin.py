from django.contrib import admin

# Register your models here.
from car_api.car_brand.models import CarBrand
from car_api.car_model.models import CarModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'name')

