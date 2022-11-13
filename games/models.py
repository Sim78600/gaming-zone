from django.db import models

# Create your models here.

class Games(models.Model):
    game_title = models.CharField(max_length=200),
    game_rating = models.FloatField(max_length=5),
    game_logo = models.ImageField(upload_to='photos')