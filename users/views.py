from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as authlogin
from django.contrib import messages

# Create your views here.
def profile(request):
    context={}
    return render(request, 'users/index.html', context)

def login(request):
    login_errors = {}
    if request.method == 'POST':
        data = request.POST
        username = data["username"]
        password = data["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            authlogin(request, user)
            return redirect('home')
        else:
            login_errors['incorrect'] = messages.error(request, "Incorrect username or password")
    context={'login_errors':login_errors}
    return render(request, 'users/login.html', context)
