from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.


# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         context = {'movie_list': movies}
#         return render(request, 'movies/movies.html', context)

class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(is_published=True)
    template_name = 'movies/movies.html'


# class MovieDetailView(View):
#     def get(self, request, slug):
#         movie = get_object_or_404(Movie, url=slug)
#         context = {'movie': movie}
#         return render(request, 'movies/movie_detail.html', context)
class MoviesDetailView(DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'movies/movie_detail.html'
