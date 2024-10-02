from django.contrib import admin
from .models import Topic, Task, Test, Classes, Choice, TestResult, Question


# Register your models here.
admin.site.register(Topic)
admin.site.register(Task)
admin.site.register(Test)
admin.site.register(Classes)
admin.site.register(Choice)
admin.site.register(TestResult)
admin.site.register(Question)
