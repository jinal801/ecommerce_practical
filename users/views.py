from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from EcommerceCRUD import settings
from users.constants import LOGIN_SUCCESS_MSG
from users.forms import SignUpForm, UserLoginForm


class DashboardView(TemplateView):
    """class for dashboard page"""
    template_name = 'dashboard.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class LoginView(SuccessMessageMixin, LoginView):
    """Login View"""
    template_name ='login.html'
    authentication_form = UserLoginForm
    success_message = LOGIN_SUCCESS_MSG


class LogoutView(LoginRequiredMixin, LogoutView):
    """Logout View"""
