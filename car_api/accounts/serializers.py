from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from car_api.accounts.models import AuthUser

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=15,
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )
    first_name = serializers.CharField(
        max_length=AuthUser.FIRST_NAME_MAX_LENGTH,
        required=False,
        write_only=True,
    )
    last_name = serializers.CharField(
        max_length=AuthUser.LAST_NAME_MAX_LENGTH,
        required=False,
        write_only=True,
    )
    email = serializers.EmailField(
        required=False,
        write_only=True,
    )
    age = serializers.IntegerField(
        required=False,
        write_only=True,
    )
    phone_number = serializers.CharField(
        max_length=AuthUser.PHONE_NUMBER_MAX_LENGTH,
        required=False,
        write_only=True,
    )
    gender = serializers.CharField(
        max_length=AuthUser.GENDER_MAX_LENGTH,
        required=False,
        write_only=True,
    )

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'age', 'phone_number', 'gender')


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # Fix issue with password in plain text
        return user

    # remove password from response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result

    def validate(self, data):
        user = UserModel(**data)
        password = data.get('password')
        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=user)

        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return super(CreateUserSerializer, self).validate(data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label='Username',
        write_only=True,
    )
    password = serializers.CharField(
        label='Password',
        style= {'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
    )
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Access denied: incorrectly entered data.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs