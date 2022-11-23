from django.shortcuts import render,get_object_or_404
from .models import game

# Create your views here.


def home(request):
    games = game.objects.all()
    data ={
        'games' : games
    }
    return render(request,'index.html',data)

def browse(request):
    games = game.objects.all()
    data ={
        'games' : games
    }
    return render(request,'browse.html',data)

def details(request, id):
    single_game = get_object_or_404(game,pk=id)
    data={
        'single_game' : single_game,
    }
    return render(request,'details.html', data)

def profile(request):
    return render(request,'profile.html')

def games(request):
    return render(request,'games.html')

def streams(request):
    return render(request,'profile.html')

def search(request):
    return render(request,'')

def categories(request):
    game_racing = game.objects.filter(game_category__icontains ='racing')
    game_puzzle = game.objects.filter(game_category__icontains='puzzle')
    game_shooting = game.objects.filter(game_category__icontains='shooting')
    game_adventure = game.objects.filter(game_category__icontains='adventure')
    game_parkour = game.objects.filter(game_category__icontains='parkour')
    data = {
        'game_racing' : game_racing ,
        'game_puzzle' : game_puzzle ,
        'game_shooting' : game_shooting,
        'game_adventure' : game_adventure,
        'game_parkour' : game_parkour,
    }
    return render(request,'categories.html',data)   