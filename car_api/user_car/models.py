from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from car_api.car_brand.models import CarBrand
from car_api.car_model.models import CarModel
from car_api.common.models import SoftDeleteModel

UserModel = get_user_model()

class UserCar(SoftDeleteModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    first_reg = models.DateField()
    odometer = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
    )
