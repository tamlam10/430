from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_movies, name='list_movies'),
    path('add/', views.add_movie, name='add_movie'),
    path('edit/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
]
