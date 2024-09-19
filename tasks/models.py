from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TopicClass5(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название темы")

    def __str__(self):
        return self.name

    def get_task_url(self):
        return f'/task_lists/{self.pk}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class TaskClass5(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название задания")
    topic = models.ForeignKey(TopicClass5, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField(verbose_name='Описание задания')

    def __str__(self):
        return self.title

    def get_task_url(self):
        return f'/task_lists/{self.pk}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос к которому относится ответ')
    choice_text = models.CharField(max_length=200, verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный?')

    def __str__(self):
        return self.question.question_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Test(models.Model):
    topic = models.ForeignKey(TopicClass5, on_delete=models.CASCADE, verbose_name='Тема', related_name='tasks_test')
    question = models.ManyToManyField(Question, verbose_name='Вопрос в тесте', related_name='questions')
    test_name = models.CharField(max_length=100, verbose_name='Имя теста')

    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест', related_name='test_results')
    score = models.IntegerField(verbose_name='Результат')

    def __str__(self):
        return f'{self.user.username} - {self.test.test_name} - {self.score}%'

    class Meta:
        verbose_name = 'Резульат теста'
        verbose_name_plural = 'Результаты тестов'
