from django.db import models


class Movie(models.Model):
    choice = [
        ("الفيلم", 'الفيلم'),
        ("المسلسل", 'المسلسل'),

    ]
    name = models.CharField(max_length=150, null=True)
    describe = models.TextField(null=True)
    date_production = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    creator = models.CharField(max_length=150, null=True)
    stars = models.CharField(max_length=150, null=True)
    image = models.URLField(null=True)
    platform = models.CharField(max_length=50, null=True)
    published = models.DateTimeField(auto_now_add=True)
    video = models.URLField(null=True)
    choice = models.CharField(max_length=50, null=True, choices=choice)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ["-published"]


class Serial(models.Model):

    choice = [
        ("الفيلم", 'الفيلم'),
        ("المسلسل", 'المسلسل'),

    ]
    name = models.CharField(max_length=150, null=True)
    describe = models.TextField(null=True)
    date_production = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    creator = models.CharField(max_length=150, null=True)
    stars = models.CharField(max_length=150, null=True)
    image = models.URLField(null=True)
    platform = models.CharField(max_length=50, null=True)
    published = models.DateTimeField(auto_now=True)
    video = models.URLField(null=True)
    choice = models.CharField(max_length=50, null=True, choices=choice)


    class Meta():
        ordering = ["-published"]

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=150, null=True)
    image = models.URLField(null=True)

    def __str__(self):
        return self.name
