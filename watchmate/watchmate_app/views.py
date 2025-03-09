# from django.shortcuts import render
# from watchmate_app.models import Movie
# # import JSON Response to send a response object
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request):
#     # Get all the movies in the database
#     movies = Movie.objects.all()
#     # This gives an error as we are just returning a list. We need to return a dictionary as JSON can only work with dictionary. 
#     # print(movies)
#     # So, return the fetched movies as a dictionary with id as movies and the value as the list of movies fetched from DB. 

#     data = {
#         'movies': list(movies.values()),
#     }

#     # Return the data as JSONResponse
#     return JsonResponse(data)


# # Define a function to return the data about a particular movie
# def movie_details(request, movieId):
#     # Get the movie details using primary key. 
#     movie = Movie.objects.get(id=movieId)
#     # Wrap this data in a dictionary and send it as Json Response
#     data = {
#         'name': movie.name,
#         'description': movie.description, 
#         'isMovieReleased': movie.isMovieReleased
#     }

#     return JsonResponse(data)

