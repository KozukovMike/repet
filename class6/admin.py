from django.contrib import admin
from .models import TaskClass6, TopicClass6, Question6, Choice6, Test6, TestResult6


# Register your models here.
@admin.register(TaskClass6)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'description')
    list_filter = ('topic',)
    search_fields = ('title', 'description')
    list_per_page = 20


@admin.register(TopicClass6)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Choice6)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('get_question_text', 'choice_text', 'is_correct')
    search_fields = ('choice_text',)
    list_filter = ('is_correct',)
    list_per_page = 20

    @staticmethod
    def get_question_text(obj):
        return obj.question.question_text
    get_question_text.short_description = 'Текст вопроса'


@admin.register(Question6)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text',)


@admin.register(Test6)
class TestAdmin(admin.ModelAdmin):
    list_display = ('topic', 'test_name', 'questions')
    list_filter = ('topic',)
    search_fields = ('test_name',)
    list_per_page = 20

    def questions(self, obj):
        return ' '.join([f'{i}) {item.question_text}' for i, item in enumerate(obj.question.all(), start=1)])
    questions.short_description = 'Вопросы'


@admin.register(TestResult6)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'score')
    list_filter = ('user', 'test')
    list_per_page = 20
