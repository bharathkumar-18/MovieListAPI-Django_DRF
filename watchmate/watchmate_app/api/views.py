from rest_framework.response import Response
from rest_framework.decorators import api_view

from watchmate_app.models import Movie
from watchmate_app.api.serializers import MovieSerializer

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view()
def movie_details(request, movieId):
    movie = Movie.objects.get(id=movieId)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

