from django.contrib import admin
from .models import TaskClass5, TopicClass5


# Register your models here.
@admin.register(TaskClass5)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(TopicClass5)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
