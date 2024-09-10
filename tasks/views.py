from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskClass5, TopicClass5


# Create your views here.
def task_page(request):
    return render(request, './task_page.html')


def class5_page(request):
    topic_list = TopicClass5.objects.all()
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'class5.html', context)
