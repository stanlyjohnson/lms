from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# from __future__ import unicode_literals
# Create your models here.

class author (models.Model):

    name = models.CharField(max_length = 50)
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    country = models.CharField(max_length=20)
    about = models.TextField(max_length = 300)

    def _str_ (self):
        return self.name
    def __unicode__ (self):
        return self.name

class book (models.Model):
    title = models.CharField(max_length = 50)
    writtenby = models.ForeignKey(author, on_delete=models.CASCADE)
    isbn = models.SlugField(max_length = 25)
    prologue = models.TextField(max_length = 500)

    def _str_ (self):
        return self.writtenby.name
    def __unicode__ (self):
        return self.writtenby.name
