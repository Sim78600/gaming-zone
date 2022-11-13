from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def browse(request):
    return render(request,'browse.html')

def details(request):
    return render(request,'details.html')

def profile(request):
    return render(request,'profile.html')

def streams(request):
    return render(request,'profile.html')

def search(request):
    return render(request,'')