from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST['email']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            print(username)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid Employee ID or Password")
            return redirect(user_login)
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')