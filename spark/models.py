from django.db import models


# Create your models here.
class WordModel(models.Model):
    word = models.CharField(max_length = 50)

WordModel(word = "aaaaa")

