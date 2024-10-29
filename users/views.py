from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        print('hello')
        print(request.POST)
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
