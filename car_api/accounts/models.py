
from django.contrib.auth import models as auth_models
from django.db import models

from car_api.accounts import managers as custom_managers


class AuthUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x, x )for x in (MALE, FEMALE, DO_NOT_SHOW)]
    GENDER_MAX_LENGTH = 15
    PHONE_NUMBER_MAX_LENGTH = 15
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateField(auto_now_add=True)
    email = models.EmailField(
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=GENDER_MAX_LENGTH,
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = custom_managers.CarUserManager()


# class Profile(models.Model):
#     FIRST_NAME_MAX_LENGTH = 15
#     LAST_NAME_MAX_LENGTH = 15
#
#     first_name = models.CharField(
#         max_length=FIRST_NAME_MAX_LENGTH,
#     )
#     last_name = models.CharField(
#         max_length=LAST_NAME_MAX_LENGTH,
#     )
#     age = models.IntegerField(
#         null=True,
#         blank=True,
#     )
#     phone_number = models.CharField(
#         max_length=15,
#         null=True,
#         blank=True,
#     )
#
#     user = models.OneToOneField(
#         AuthUser,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'