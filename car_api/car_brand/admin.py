from django.contrib import admin

from car_api.car_brand.models import CarBrand


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
