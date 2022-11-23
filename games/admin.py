from django.contrib import admin
from .models import game


class gameAdmin(admin.ModelAdmin):
    list_display = ('id','game_logo','game_title','game_logo')

# Register your models here.

admin.site.register(game,gameAdmin)


