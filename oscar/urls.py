from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("Amazon", amazon, name="amazon"),
    path("AmazonMovies", amazon_movies, name="amazon_movies"),
    path("AmazonSeries", amazon_series, name="amazon_series"),
    path("netflix", netflix, name="netflix"),
    path("netflixMovies", netflix_movies, name="netflix_movies"),
    path("netflixSeries", netflix_series, name="netflix_series"),
    path("watch/<str:slug>", watch_page, name="watch"),

]
