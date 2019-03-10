from django.urls import path
from . import views

urlpatterns = [
    path('', views.cate, name='cate'),
    path('add/', views.add_cate, name='add_cate'),
    path('edit/<int:cate_id>/', views.edit_cate, name='edit_cate'),
    path('delete/<int:cate_id>/', views.delete_cate, name='delete_cate'),
]
