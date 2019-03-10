from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.movie, name='movie'),
    path('<int:movie_id>/comment/', include('comments.urls')),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('delete/<int:movie_id>', views.delete_movie, name='delete_movie'),
]
