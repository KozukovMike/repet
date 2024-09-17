from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskClass5, TopicClass5
from django.shortcuts import render, redirect
from .models import Question, Choice


# Create your views here.
@login_required(login_url='login')
def task_page(request):
    return render(request, './task_page.html')


@login_required(login_url='login')
def class5_page(request):
    topic_list = TopicClass5.objects.all()
    context = {
        'topic_list': topic_list,
    }
    print(topic_list[0])
    return render(request, 'class5.html', context)


@login_required(login_url='login')
def test_view(request):
    if request.method == 'POST':
        total_questions = Question.objects.count()
        score = 0
        for q in Question.objects.all():
            choice_id = request.POST.get(f'question_{q.id}')
            if choice_id:
                selected_choice = Choice.objects.get(pk=choice_id)
                if selected_choice.is_correct:
                    score += 1
        context = {
            'total_questions': total_questions,
            'score': score,
        }
        return render(request, 'test_template.html', context)

    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'test_template.html', context)
