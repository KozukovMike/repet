from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'base.html')


def custom_logout(request):
    logout(request)
    return redirect('home')
