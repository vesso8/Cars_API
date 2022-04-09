from django.db import models
from django.utils import timezone

from car_api.common.managers import SoftDeleteManager


class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(null=True,blank=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True