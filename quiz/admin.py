from django.contrib import admin
from .models import Question
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'difficulty', 'points', 'is_premium')
    list_filter = ('difficulty', 'is_premium')
    search_fields = ('question_text',)