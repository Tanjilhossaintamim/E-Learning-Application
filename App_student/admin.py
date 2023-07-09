from django.contrib import admin
from App_student.models import AnswarQuestion, AskedQuestion
# Register your models here.


@admin.register(AskedQuestion)
class AskedQuestionAdmin(admin.ModelAdmin):
    '''Admin View for AskedQuestion'''

    list_display = ('id', 'student', 'subject', 'description')
    list_per_page = 10


@admin.register(AnswarQuestion)
class AnswarQuestionAdmin(admin.ModelAdmin):
    '''Admin View for AnswarQuestion'''

    list_display = ('id', 'teacher', 'question', 'answar')
