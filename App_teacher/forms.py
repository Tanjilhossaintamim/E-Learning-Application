from django.forms import ModelForm
from .models import Articale, Quiz


class ArticalForm(ModelForm):
    class Meta:
        model = Articale
        exclude = ['author']


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        exclude = ['teacher']
