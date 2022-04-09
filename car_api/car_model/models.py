from django.db import models

from django.db import models

from car_api.car_brand.models import CarBrand
from car_api.common.models import SoftDeleteModel


class CarModel(SoftDeleteModel):
    CAR_MODEL_NAME_MAX_LENGTH = 25

    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=CAR_MODEL_NAME_MAX_LENGTH,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.car_brand} - {self.name}'