
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/api/', include('car_api.accounts.urls')),
    path('brands/', include('car_api.car_brand.urls')),
    path('models/', include('car_api.car_model.urls')),
    path('users/', include('car_api.user_car.urls')),
]
