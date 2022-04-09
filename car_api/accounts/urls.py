from django.urls import path

from car_api.accounts.views import RegisterView, LoginView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
)