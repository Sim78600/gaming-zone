from django.db import models

# Create your models here.

class game(models.Model):
    game_logo = models.ImageField(upload_to='photos')
    game_title = models.CharField(max_length=255)
    game_rating = models.FloatField()
    game_link = models.CharField(max_length=255,default='')
    game_category = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.game_title
    
