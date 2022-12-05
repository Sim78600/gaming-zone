from django.shortcuts import render , redirect

# Create your views here.

def login(request):
    return render(request,'login.html')

def logout(request):
    return redirect('index.html')

def signup(request):
    if request.method == 'POST':
        print('this is sign up method')
        return redirect('signup')
    else:
        return render(request,'register.html')

def dashboard(request):
    return render(request,'profile.html')