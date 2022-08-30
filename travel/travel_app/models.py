from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()



class Route(models.Model):
    name = models.CharField(max_length=255)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    places = models.ForeignKey("Place", on_delete=models.CASCADE)
    description = models.TextField()
    time = models.CharField(max_length=30)
    image = models.ImageField()


class Place(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField()
    feedback = models.TextField(blank=False)