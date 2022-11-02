from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        context = {'movie_list': movies}
        return render(request, 'movies/movie_list.html', context)

