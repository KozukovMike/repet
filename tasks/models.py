from django.db import models


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
