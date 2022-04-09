
from django.db import models

from car_api.common.models import SoftDeleteModel


class CarBrand(SoftDeleteModel):
    CAR_BRAND_MAX_LENGTH = 25
    name = models.CharField(
        max_length=CAR_BRAND_MAX_LENGTH,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f'{self.name}'

