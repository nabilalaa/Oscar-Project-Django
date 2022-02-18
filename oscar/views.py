from django.shortcuts import render
from .models import *
from django.template.defaultfilters import slugify


def index(request):
    context = {
        "movies_netflix": Movie.objects.filter(platform="netflix"),
        "movies_amazon": Movie.objects.filter(platform="amazon"),
        "series_netflix": Serial.objects.filter(platform="netflix"),
        "series_amazon": Serial.objects.filter(platform="amazon"),
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


def watch_page(request, slug):
    context = {
        "slugs": Movie.objects.filter(name=slug.replace("-", " ")),
        "test": slugify(slug)
    }
    return render(request, "watch_page.html", context)
