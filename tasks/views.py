import math

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskClass5, TopicClass5
from django.shortcuts import render, redirect
from .models import Question, Choice, Test, TestResult


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
def test_view(request, test_id):

    if request.method == 'POST':
        form_test_id = request.POST.get('test_id')
        test = Test.objects.get(pk=form_test_id)
        total_questions = test.question.count()
        score = 0

        for question in test.question.all():
            choice_id = request.POST.get(f'question_{question.id}')

            if choice_id:
                selected_choice = Choice.objects.get(pk=choice_id)

                if selected_choice.is_correct:
                    score += 1
        print(len(test.question.all()))
        test_result = TestResult(user=request.user, test=test, score=math.trunc(score / len(test.question.all()) * 100))
        test_result.save()
        context = {
            'total_questions': total_questions,
            'score': str(score),
            'test_id': form_test_id,
            'test': test,
        }

        return render(request, 'test_template.html', context)

    test = Test.objects.get(pk=test_id)
    context = {
        'test': test,
    }
    return render(request, 'test_template.html', context)
