# Usersite/urls.py
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import SignUpView, DashboardView

# app_name = 'Users'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('signup/', SignUpView.as_view(), name='signup'),
]