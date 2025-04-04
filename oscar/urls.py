from django.urls import path
from .views import *  # noqa: F403

urlpatterns = [
    path("", index, name="home"),  # noqa: F405
    path("movies", movies, name="movies"),
    path("series", series, name="series"),
    path("Amazon", amazon, name="amazon"),
    path("AmazonMovies", amazon_movies, name="amazon_movies"),
    path("AmazonSeries", amazon_series, name="amazon_series"),
    path("netflix", netflix, name="netflix"),
    path("netflixMovies", netflix_movies, name="netflix_movies"),
    path("netflixSeries", netflix_series, name="netflix_series"),
    path("watch_movies/<str:item>", watch_movies, name="watch_movies"),
    path("watch_series/<str:item>", watch_series, name="watch_series"),
    path(
        "watch/<str:series>/<int:episode>",
        watch_series_episode,
        name="watch_series_episode",
    ),
    path("register", register, name="register"),
    path("login", log__in, name="login"),
    path("logout", log__out, name="logout"),
    path("favourite/<str:username>", favourite, name="favourite"),
    path("delete/<str:movies>/<str:username>", delete, name="delete"),
]
