from django.conf import urls
from django.urls import path

from .views import SignInView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),

]
