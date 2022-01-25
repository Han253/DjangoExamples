from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    year = models.IntegerField()
    cost = models.IntegerField()
    author =  models.ForeignKey(Author, on_delete=models.CASCADE)


