from rest_framework import serializers
from rest_framework.authtoken.admin import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'password')
