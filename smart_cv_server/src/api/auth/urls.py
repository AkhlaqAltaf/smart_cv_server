# urls.py
from django.urls import path
from .views import CustomLoginView , GetUserFromTokenView , UserCreateView

app_name = 'auth'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('get_user/', GetUserFromTokenView.as_view(), name='get_user'),
    path('register/', UserCreateView.as_view(), name='register'),


]

