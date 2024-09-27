from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import ContentHtmlMain


# Create your views here.
@login_required(login_url='login')
def home(request):
    content = ContentHtmlMain.objects.all()
    context = {
        'content': content
    }
    return render(request, 'home.html', context)


def custom_logout(request):
    logout(request)
    return redirect('home')
