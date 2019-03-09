from django.urls import path, include
from .views import detail

app_name = 'movies'

urlpatterns = [
    path('1/', detail, name='detail'),
]