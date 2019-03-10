from django.db import models
from movies.models import Movie

# Create your models here.
class Comment(models.Model):
   username = models.CharField(max_length=100)
   movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
   content = models.CharField(max_length=500)

   def __str__(self):
       return self.title
