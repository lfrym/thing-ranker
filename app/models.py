from django.db import models

# Create your models here.
class Nouns(models.Model):
    noun_text = models.CharField(max_length=200)

class Votes(models.Model):
    noun = models.ForeignKey(Nouns, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)