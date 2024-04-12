from django.urls import path

from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView
)

app_name = 'auth'
urlpatterns = [
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
]

