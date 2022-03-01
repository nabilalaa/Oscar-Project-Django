from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=150, null=True)
    describe = models.TextField(null=True)
    category = models.CharField(max_length=150, null=True)
    date_production = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    durations = models.IntegerField(null=True)
    creator = models.CharField(max_length=150, null=True)
    stars = models.CharField(max_length=150, null=True)
    image = models.URLField(null=True)
    platform = models.CharField(max_length=50, null=True)
    published = models.DateTimeField(auto_now_add=True)
    video = models.URLField(null=True)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ["-published"]


class Show(models.Model):
    name = models.CharField(max_length=150, null=True)
    describe = models.TextField(null=True)
    category = models.CharField(max_length=150, null=True)
    date_production = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    durations = models.IntegerField(null=True)
    creator = models.CharField(max_length=150, null=True)
    stars = models.CharField(max_length=150, null=True)
    image = models.URLField(null=True)
    platform = models.CharField(max_length=50, null=True)
    published = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ["-published"]

    def __str__(self):
        return self.name


class Episode(models.Model):
    name = models.ForeignKey(Show, null=True, on_delete=models.CASCADE)
    video = models.URLField(null=True)
    number = models.IntegerField(null=True)

    def __str__(self):
        return f" {self.name}  ( الحلقة -->  {self.number} )"


class Banner(models.Model):
    name = models.CharField(max_length=150, null=True)
    image = models.URLField(null=True)

    def __str__(self):
        return self.name


class Favourite(models.Model):
    name = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rate = models.FloatField(null=True)
    image = models.URLField(null=True)

    def __str__(self):
        return f"{self.name}"
