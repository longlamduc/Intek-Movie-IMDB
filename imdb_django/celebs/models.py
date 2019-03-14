from django.db import models

# Create your models here.
class Celeb(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   birthday = models.DateTimeField()
   sex = models.CharField(max_length=6)
   nationality = models.CharField(max_length=100)
   is_alive = models.CharField(max_length=3)
   avatar = models.CharField(max_length=200, blank=True)

   def __str__(self):
       return "%s %s" % (self.first_name, self.last_name)

   class Meta:
       ordering = ('first_name', 'last_name', )
