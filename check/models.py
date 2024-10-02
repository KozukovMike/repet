from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Classes(models.Model):

    class_number = models.IntegerField(verbose_name='Номер класса')

    def __str__(self):
        return f'{self.class_number}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Topic(models.Model):

    topic_name = models.CharField(max_length=100, verbose_name='Название темы')
    class_number_id = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='ID номера класса', related_name='topic_classes')

    def __str__(self):
        return self.topic_name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Task(models.Model):

    task_name = models.CharField(max_length=100, verbose_name='Имя задания')
    topic_name_id = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='ID названия темы', related_name='task_topics')
    description = models.TextField(verbose_name='Текст задания')

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос для теста'
        verbose_name_plural = 'Вопросы для теста'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос к которому относится ответ', related_name='choice_questions')
    choice_text = models.CharField(max_length=200, verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный?')

    def __str__(self):
        return self.question.question_text

    class Meta:
        verbose_name = 'Ответ для теста'
        verbose_name_plural = 'Ответы для теста'


class Test(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема', related_name='test_topic')
    question = models.ManyToManyField(Question, verbose_name='Вопрос в тесте', related_name='test_questions')
    test_name = models.CharField(max_length=100, verbose_name='Имя теста')

    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест', related_name='test_results_test')
    score = models.IntegerField(verbose_name='Результат')

    def __str__(self):
        return f'{self.user.username} - {self.test.test_name} - {self.score}%'

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'
