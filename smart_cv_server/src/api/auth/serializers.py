# serializers.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer

from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField(required=True)
    username = None  # Make username field not required

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


    class UserSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        username = serializers.CharField(max_length=150)
        email = serializers.EmailField()






class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password']
        )

        user.save()
        return user
