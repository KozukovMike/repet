import math
import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Choice, Classes, Topic, Test, TestResult, Task, Question


logger = logging.getLogger(__name__)


@login_required(login_url='login')
def task_page(request):
    return render(request, 'task_page.html')


@login_required(login_url='login')
def class5_page(request):
    try:
        class_list = Classes.objects.all()[0]
        context = {
            'class_list': class_list,
        }
        return render(request, 'class.html', context)

    except IndexError:
        logger.error('IndexError: Класс с индексом 0 не найден.')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)

    except Exception as e:
        logger.error(f'Ошибка в функции class5_page: {e}')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)


@login_required(login_url='login')
def class6_page(request):
    try:
        class_list = Classes.objects.all()[1]
        context = {
            'class_list': class_list,
        }
        return render(request, 'class.html', context)

    except IndexError:
        logger.error('IndexError: Класс с индексом 1 не найден.')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)

    except Exception as e:
        logger.error(f'Ошибка в функции class6_page: {e}')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)


@login_required(login_url='login')
def class7_page(request):
    try:
        class_list = Classes.objects.all()[2]
        context = {
            'class_list': class_list,
        }
        return render(request, 'class.html', context)

    except IndexError:
        logger.error('IndexError: Класс с индексом 2 не найден.')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)

    except Exception as e:
        logger.error(f'Ошибка в функции class7_page: {e}')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)


@login_required(login_url='login')
def class8_page(request):
    try:
        class_list = Classes.objects.all()[3]
        context = {
            'class_list': class_list,
        }
        return render(request, 'class.html', context)

    except IndexError:
        logger.error('IndexError: Класс с индексом 3 не найден.')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)

    except Exception as e:
        logger.error(f'Ошибка в функции class8_page: {e}')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)


@login_required(login_url='login')
def class9_page(request):
    try:
        class_list = Classes.objects.all()[4]
        context = {
            'class_list': class_list,
        }
        return render(request, 'class.html', context)

    except IndexError:
        logger.error('IndexError: Класс с индексом 4 не найден.')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)

    except Exception as e:
        logger.error(f'Ошибка в функции class9_page: {e}')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)


@login_required(login_url='login')
def class10_page(request):
    try:
        class_list = Classes.objects.all()[5]
        context = {
            'class_list': class_list,
        }
        return render(request, 'class.html', context)

    except IndexError:
        logger.error('IndexError: Класс с индексом 5 не найден.')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)

    except Exception as e:
        logger.error(f'Ошибка в функции class10_page: {e}')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)


@login_required(login_url='login')
def class11_page(request):
    try:
        class_list = Classes.objects.all()[6]
        context = {
            'class_list': class_list,
        }
        return render(request, 'class.html', context)

    except IndexError:
        logger.error('IndexError: Класс с индексом 6 не найден.')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)

    except Exception as e:
        logger.error(f'Ошибка в функции class11_page: {e}')
        context = {
            'error': 'Произошла ошибка обратитесь к администратору'
        }
        return render(request, 'errors/error.html', context)


@login_required(login_url='login')
def test_view(request, test_id):
    try:
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
            test_result = TestResult(user=request.user, test=test, score=math.trunc(score / len(test.question.all()) * 100))
            test_result.save()
            context = {
                'total_questions': total_questions,
                'score': str(score),
                'test_id': form_test_id,
                'test': test,
            }

            return render(request, 'test.html', context)

        test = Test.objects.get(pk=test_id)
        context = {
            'test': test,
        }
        return render(request, 'test.html', context)

    except Test.DoesNotExist as e:
        logger.error(f'{e}. Тест не найден. Функция test_view')
        return render(request, 'errors/error.html', {'error': 'Произошла ошибка обратитесь к администратору'})

    except Choice.DoesNotExist as e:
        logger.error(f'{e}. Выбранного варианта не существует. Функция test_view')
        return render(request, 'errors/error.html', {'error': 'Произошла ошибка обратитесь к администратору'})

    except Exception as e:
        logger.error(f'{e}. Функция test_view')
        return render(request, 'errors/error.html', {'error': 'Произошла ошибка обратитесь к администратору'})
