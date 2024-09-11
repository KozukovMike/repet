from django.db import models


# Create your models here.
class TopicClass5(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название темы")

    def __str__(self):
        return self.name

    def get_task_url(self):
        return f'/task_lists/{self.pk}'

    class Meta:
        verbose_name = 'Тема для 5 класса'
        verbose_name_plural = 'Темы для 5 класса'


class TaskClass5(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название задания")
    topic = models.ForeignKey(TopicClass5, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField(verbose_name='Описание задания')

    def __str__(self):
        return self.title

    def get_task_url(self):
        return f'/task_lists/{self.pk}'

    class Meta:
        verbose_name = 'Задание для 5 класса'
        verbose_name_plural = 'Задание для 5 класса'
