from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Choice, Classes, Topic, Test, TestResult, Task, Question


# Create your views here.
@login_required(login_url='login')
def task_page(request):
    return render(request, 'check/task_page.html')


@login_required(login_url='login')
def class5_page(request):
    class_list = Classes.objects.all()[0]
    context = {
        'class_list': class_list,
    }
    return render(request, 'check/class.html', context)


@login_required(login_url='login')
def class6_page(request):
    class_list = Topic.objects[1]
    context = {
        'class_list': class_list,
    }
    return render(request, 'check/class.html', context)


@login_required(login_url='login')
def test_view_5(request, test_id):

    if request.method == 'POST':
        form_test_id = request.POST.get('test_id')
        test = Test5.objects.get(pk=form_test_id)
        total_questions = test.question.count()
        score = 0

        for question in test.question.all():
            choice_id = request.POST.get(f'question_{question.id}')

            if choice_id:
                selected_choice = Choice5.objects.get(pk=choice_id)

                if selected_choice.is_correct:
                    score += 1
        test_result = TestResult5(user=request.user, test=test, score=math.trunc(score / len(test.question.all()) * 100))
        test_result.save()
        context = {
            'total_questions': total_questions,
            'score': str(score),
            'test_id': form_test_id,
            'test': test,
        }

        return render(request, 'tests/test5.html', context)

    test = Test5.objects.get(pk=test_id)
    context = {
        'test': test,
    }
    return render(request, 'tests/test5.html', context)
