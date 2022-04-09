from django.contrib.auth import views as auth_views, login, get_user_model
from rest_framework import generics as api_generic_views, permissions
from rest_framework import generics as api_generics_views, permissions, status
from rest_framework import views as api_views
from rest_framework.response import Response

from car_api.accounts.models import AuthUser
from car_api.accounts.serializers import CreateUserSerializer
from . import serializers

UserModel = get_user_model()

class RegisterView(api_generics_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (
        permissions.AllowAny,
    )

class LoginView(api_views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)