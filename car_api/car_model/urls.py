from django.urls import path

from car_api.car_model.views import CarModelCreateView, CarModelDetailsView, CarModelListView

urlpatterns =(
    path('list/', CarModelListView.as_view(), name='car model list'),
    path('create/', CarModelCreateView.as_view(), name='car model create'),
    path('<int:pk>/', CarModelDetailsView.as_view(), name='car model details'),
)