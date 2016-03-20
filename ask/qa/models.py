from __future__ import unicode_literals

from django.db import models
from django.contrib import auth


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(auth.models.User)
    likes = models.ManyToManyField(auth.models.User)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.OneToOneField(Question)
    author = models.ForeignKey(auth.models.User)
