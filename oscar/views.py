from django.shortcuts import render
from .models import *
from django.template.defaultfilters import slugify


def index(request):
    context = {
        "movies_netflix": Movie.objects.filter(platform="netflix"),
        "movies_amazon": Movie.objects.filter(platform="amazon"),
        "series_netflix": Show.objects.filter(platform="netflix"),
        "series_amazon": Show.objects.filter(platform="amazon"),
        "banners": Banner.objects.all()

    }
    return render(request, "index.html", context)


def amazon(request):
    context = {

    }
    return render(request, "amazon.html", context)


def amazon_movies(request):
    context = {

    }
    return render(request, "amazon_movies.html", context)


def amazon_series(request):
    context = {

    }
    return render(request, "amazon_series.html", context)


def netflix(request):
    context = {

    }
    return render(request, "netflix.html", context)


def netflix_movies(request):
    context = {

    }
    return render(request, "netflix_movies.html", context)


def netflix_series(request):
    context = {

    }
    return render(request, "netflix_series.html", context)


def watch_movies(request, movies):
    context = {
        "movies": Movie.objects.filter(name=movies.replace("-", " ")),
    }
    return render(request, "watch_movies.html", context)


def watch_series(request, series, ):
    context = {
        "shows": Show.objects.filter(name=series.replace("-", " ")),
        "episodes": Episode.objects.filter(name=series.replace("-", " "))
    }
    return render(request, "watch_series.html", context)


def watch_series_episode(request, series, episode):
    context = {
        "shows": Show.objects.filter(name=series.replace("-", " ")),
        "episodes": Episode.objects.filter(name=series.replace("-", " ")),
        "current_episode": Episode.objects.filter(name=series.replace("-", " "), number=episode),

    }
    return render(request, "watch_series_episode.html", context)
