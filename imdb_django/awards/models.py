from django.db import models
from movies.models import Movie
from celebs.models import Celeb

# Create your models here.
class Award(models.Model):
    KIND_CHOICES = (
        ('Celeb', 'Celeb'),
        ('Movie', 'Movie'),
    )
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=5, choices=KIND_CHOICES)
    date = models.DateTimeField()
    movies = models.ManyToManyField(Movie)
    celebs = models.ManyToManyField(Celeb)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'kind')
