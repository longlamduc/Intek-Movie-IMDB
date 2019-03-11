from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.movie, name='movie'),
    path('<int:movie_id>/comment/', include('comments.urls')),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('<int:movie_id>/edit', views.edit_movie, name='movie_edit'),
    path('<int:movie_id>/delete', views.delete_movie, name='movie_delete'),
]
