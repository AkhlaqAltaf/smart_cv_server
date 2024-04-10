# views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate

from src.apps.accounts.forms import SignupForm, SigninForm


class SignInView(LoginView):
    form_class = SigninForm
    template_name = 'signin.html'
    success_url = reverse_lazy('....')


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('website:home')