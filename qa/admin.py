"""
[과제 3] qa/admin.py
TODO: Question과 Answer 모델을 admin에 등록하세요.
"""
from django.contrib import admin
from .models import Question, Answer

# TODO: Question 모델을 admin에 등록하세요
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')

# TODO: Answer 모델을 admin에 등록하세요
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)
