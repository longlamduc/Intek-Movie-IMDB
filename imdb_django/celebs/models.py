from django.db import models

# Create your models here.
class Celeb(models.Model):
   GENDER_CHOICES = (
       ('M', 'Male'),
       ('F', 'Female'),
   )
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   birthday = models.DateTimeField()
   sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
   nationality = models.CharField(max_length=100)
   is_alive = models.BooleanField(default=True)

   def __str__(self):
       return "%s %s" % (self.first_name, self.last_name)

   class Meta:
       ordering = ('first_name', 'last_name', )
