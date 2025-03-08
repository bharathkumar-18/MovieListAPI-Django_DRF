from django.urls import path, include
from .views import movie_list, movie_details

urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:movieId>/', movie_details, name='movie-details')
]
