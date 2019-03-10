from django.urls import path
from . import views

urlpatterns = [
    path('', views.celeb, name='celeb'),
    path('<int:celeb_id>/', views.celeb_detail, name='celeb_detail'),
    path('add/', views.add_celeb, name='add_celeb'),
    path('edit/<int:celeb_id>/', views.edit_celeb, name='edit_celeb'),
    path('delete/<int:celeb_id>', views.delete_celeb, name='delete_celeb'),
]
