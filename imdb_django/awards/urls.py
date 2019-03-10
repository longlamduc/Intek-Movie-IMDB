from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.award, name='award'),
    path('<int:award_id>/', views.award_detail, name='award_detail'),
    path('add/', views.add_award, name='add_award'),
    path('edit/<int:award_id>/', views.edit_award, name='edit_award'),
    path('delete/<int:award_id>', views.delete_award, name='delete_award'),
]
