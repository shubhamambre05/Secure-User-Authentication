from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# user password shu@@##12

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect ("/login")
    return render (request, "index.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(username=username, password=password)
        if User is not None:
           login(request,User)
           return redirect("/")
        else:
           return render (request,"login.html")
    
    
    return render (request,"login.html")

def logoutUser(request):
    return redirect("/login")