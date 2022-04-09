from django.urls import path

from car_api.user_car.views import UserCarListView, UserCarDetailsView, UserCarCreateView

urlpatterns =(
    path('list/', UserCarListView.as_view(), name='user car list'),
    path('create/', UserCarCreateView.as_view(), name='user car create'),
    path('<int:pk>/', UserCarDetailsView.as_view(), name='user details'),
)