# views.py
from rest_framework import status
from rest_framework.authtoken.models import Token
from dj_rest_auth.views import LoginView as BaseLoginView
from .serializers import CustomLoginSerializer, UserCreateSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..users.serializers import UserSerializer


class CustomLoginView(BaseLoginView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class GetUserFromTokenView(APIView):
    print("REQUEST HIT ")
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("REQUEST ",request.user)
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)



class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


