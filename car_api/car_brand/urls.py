from django.urls import path

from car_api.car_brand.views import CarBrandDetailsView, CarBrandListView, CarBrandCreateView

urlpatterns =(
    path('list/', CarBrandListView.as_view(), name='list brands'),
    path('create/', CarBrandCreateView.as_view(), name='create brands'),
    path('<int:pk>/', CarBrandDetailsView.as_view(), name='car brand details'),
)