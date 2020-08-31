from django.contrib import admin
from .models import Answer, Question, Story

admin.site.register(Answer)
admin.site.register(Story)
admin.site.register(Question)

# Register your models here.

