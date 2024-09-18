from django.contrib import admin
from .models import TaskClass5, TopicClass5, Question, Choice, Test


# Register your models here.
@admin.register(TaskClass5)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(TopicClass5)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('get_question_text', 'choice_text', 'is_correct')

    @staticmethod
    def get_question_text(obj):
        return obj.question.question_text
    get_question_text.short_description = 'Текст вопроса'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text',)


admin.site.register(Test)
