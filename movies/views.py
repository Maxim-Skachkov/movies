from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import *

# Create your views here.


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        context = {'movie_list': movies}
        return render(request, 'movies/movies.html', context)


class MovieDetailView(View):
    def get(self, request, slug):
        movie = get_object_or_404(Movie, url=slug)
        context = {'movie': movie}
        return render(request, 'movies/movie_detail.html', context)