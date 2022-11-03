from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name='mainpage'),
    path('movie/<slug:slug>', views.MoviesDetailView.as_view(), name='movie'),
    ]