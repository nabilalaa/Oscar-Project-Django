from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    describe = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    date_production = models.IntegerField(null=True, blank=True)
    rate = models.CharField(max_length=5, null=True, blank=True)
    durations = models.IntegerField(null=True, blank=True)
    creator = models.CharField(max_length=150, null=True, blank=True)
    stars = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to="Movies", null=True, blank=True)
    imageUrl = models.URLField(verbose_name="imageurl", null=True, blank=True)

    platform = models.CharField(max_length=50, null=True, blank=True)
    published = models.DateTimeField(auto_now=True, blank=True)
    video = models.URLField(null=True,blank=True)
    iframe = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-published"]


class Show(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    describe = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    date_production = models.IntegerField(null=True, blank=True)
    rate = models.CharField(max_length=5, null=True, blank=True)
    durations = models.IntegerField(null=True, blank=True)
    creator = models.CharField(max_length=150, null=True, blank=True)
    stars = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to="Series", null=True, blank=True)
    imageUrl = models.URLField(verbose_name="imageurl", null=True, blank=True)

    platform = models.CharField(max_length=50, null=True, blank=True)
    published = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.name


class Episode(models.Model):
    name = models.ForeignKey(Show, null=True, on_delete=models.CASCADE)
    video = models.URLField(null=True, blank=True)
    iframe = models.URLField(null=True, blank=True)

    number = models.IntegerField(null=True)

    def __str__(self):
        return f" {self.name}  ( الحلقة -->  {self.number} )"


class Banner(models.Model):
    name = models.CharField(max_length=150, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Favourite(models.Model):
    name = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rate = models.CharField(max_length=5, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"
