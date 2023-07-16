from django.contrib import admin
from .models import Articale, Quiz, QuizAnswar, Catagory

# Register your models here.


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    '''Admin View for Catagory'''

    list_display = ('id', 'name', 'create_at')
    list_per_page = 10


@admin.register(Articale)
class ArticaleAdmin(admin.ModelAdmin):
    '''Admin View for Articale'''

    list_display = ('id', 'title', 'published_at', 'update_at')
    list_per_page = 10


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    '''Admin View for Quiz'''

    list_display = ('id', 'teacher', 'quiz_question', 'option_1',
                    'option_2', 'option_3', 'option_4', 'correct_ans')
    list_per_page = 10


@admin.register(QuizAnswar)
class QuizAnswarAdmin(admin.ModelAdmin):
    '''Admin View for QuizAnswar'''

    list_display = ('id', 'user', 'quiz')
