from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    context = {
        "movies_netflix": Movie.objects.filter(platform="netflix"),
        "movies_amazon": Movie.objects.filter(platform="amazon"),
        "series_netflix": Show.objects.filter(platform="netflix"),
        "series_amazon": Show.objects.filter(platform="amazon"),
        "banners": Banner.objects.all()
    }
    return render(request, "index.html", context)


def movies(request):
    context = {
        "movies_netflix": Movie.objects.filter(platform="netflix"),
        "movies_amazon": Movie.objects.filter(platform="amazon"),
    }
    return render(request, "movies.html", context)


def series(request):
    context = {
        "series_netflix": Show.objects.filter(platform="netflix"),
        "series_amazon": Show.objects.filter(platform="amazon"),
    }
    return render(request, "series.html", context)


def amazon(request):
    context = {
        "movies_amazon": Movie.objects.filter(platform="amazon"),
        "series_amazon": Show.objects.filter(platform="amazon"),

    }
    return render(request, "amazon.html", context)


def amazon_movies(request):
    context = {

        "movies_amazon": Movie.objects.filter(platform="amazon"),

    }
    return render(request, "amazon_movies.html", context)


def amazon_series(request):
    context = {
        "series_amazon": Show.objects.filter(platform="amazon"),

    }
    return render(request, "amazon_series.html", context)


def netflix(request):
    context = {
        "series_netflix": Show.objects.filter(platform="netflix"),
        "movies_netflix": Movie.objects.filter(platform="netflix"),

    }
    return render(request, "netflix.html", context)


def netflix_movies(request):
    context = {
        "movies_netflix": Movie.objects.filter(platform="netflix"),

    }
    return render(request, "netflix_movies.html", context)


def netflix_series(request):
    context = {
        "series_netflix": Show.objects.filter(platform="netflix"),

    }
    return render(request, "netflix_series.html", context)


def watch_movies(request, movies):
    name_movie = request.POST.get("name")
    username = request.POST.get("username")
    rate = request.POST.get("rate")
    image = request.POST.get("image")
    if request.method == "POST" and name_movie and username and image and rate:
        if Favourite.objects.filter(name=name_movie):
            messages.error(request, "تم الاضافة")
            print(request.POST)
        else:
            Favourite.objects.create(user_id=username, name=name_movie, rate=float(rate), image=image)
    context = {
        "movies": Movie.objects.filter(name=movies.replace("-", " ")),
    }
    return render(request, "watch_movies.html", context)


def watch_series(request, series):
    name_series = request.POST.get("name")
    username = request.POST.get("username")
    rate = request.POST.get("rate")
    image = request.POST.get("image")
    print(request.POST)

    if request.method == "POST" and name_series and username and image and rate:
        if Favourite.objects.filter(name=name_series):
            messages.error(request, "تم الاضافة مسبقا")
        else:
            Favourite.objects.create(user_id=username, name=name_series, rate=float(rate), image=image)
            messages.error(request, "تم الاضافة")

    context = {
        "shows": Show.objects.filter(name=series.replace("-", " ")),
        "episodes": Episode.objects.filter(name__name=series.replace("-", " "))
    }
    return render(request, "watch_series.html", context)


def watch_series_episode(request, series, episode):
    name_series = request.POST.get("name")
    username = request.POST.get("username")
    rate = request.POST.get("rate")
    image = request.POST.get("image")
    print(image)
    if request.method == "POST" and name_series and username and image and rate:
        if Favourite.objects.filter(name=name_series):
            messages.error(request, "تم الاضافة")
            print(request.POST)
        else:
            Favourite.objects.create(user_id=username, name=name_series, rate=float(rate), image=image)
    context = {
        "shows": Show.objects.filter(name=series.replace("-", " ")),
        "episodes": Episode.objects.filter(name__name=series.replace("-", " ")),
        "current_episode": Episode.objects.filter(name__name=series.replace("-", " "), number=episode)

    }
    return render(request, "watch_series_episode.html", context)


def register(request):
    username = request.POST.get("username")

    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    re_password = request.POST.get("re_password")

    if request.method == "POST":
        if User.objects.filter(username=username):

            messages.error(request, "هذا الاسم موجود بالفعل")
        #
        elif len(password) == len(re_password) and username and first_name and last_name and email and password and len(
                password) >= 8:
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            ).save()

            return redirect("login")

        else:
            messages.error(request, "لم يتم التسجيل")

    context = {

    }
    return render(request, "sign__in.html", context)


def log__in(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if request.method == "POST" and username and password:

        if user:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "إسم المستخدم او كلمة السر غير صحيحة")

    return render(request, "login.html")


def log__out(request):
    logout(request)
    return redirect("home")


def favourite(request, username):
    context = {
        "favourites": Favourite.objects.filter(user__username=username),
    }
    return render(request, "favourite.html", context)


def delete(request, movies,username):
    print( username)
    Favourite.objects.get(name=movies).delete()
    return redirect("favourite", username="nabil")
