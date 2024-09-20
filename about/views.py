from django.shortcuts import render
from .models import ContentHtmlAbout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def about(request):
    content = ContentHtmlAbout.objects.all()
    context = {
        'content': content
    }
    return render(request, 'about.html', context)
