from rest_framework import viewsets, permissions
from rest_framework.authtoken.admin import User

from src.api.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class =UserSerializer
