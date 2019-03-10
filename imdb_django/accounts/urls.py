from django.urls import path
from django.views.generic import TemplateView
from .views import register, loginview, logoutview
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path("register/", register, name='register'),
    path("login/", loginview, name='login'),
    path("logout/", logoutview, name='logout')
]
