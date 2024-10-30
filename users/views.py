from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomLogingForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            response = redirect('home')
            response.set_cookie('username', user.username)
            return response
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def loging(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = redirect('home')
            response.set_cookie('username', user.username)
            return response
    else:
        form = AuthenticationForm()

    return render(request, 'registration/custom_login.html', {'form': form})
