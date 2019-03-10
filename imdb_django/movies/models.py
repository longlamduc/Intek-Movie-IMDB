from django.db import models
from category.models import Category
from celebs.models import Celeb
# Create your models here.

class Movie(models.Model):
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=500, default="")
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   release_date = models.DateTimeField()
   logo = models.CharField(max_length=200, null=True, blank=True)
   trailer = models.CharField(max_length=200, blank=True)
   celebs = models.ManyToManyField(Celeb, blank=True)

   def __str__(self):
       return self.title

   class Meta:
       ordering = ('title', )
