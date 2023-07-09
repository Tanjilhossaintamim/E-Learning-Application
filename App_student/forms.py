from django import forms
from .models import AskedQuestion, AnswarQuestion


class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = AskedQuestion
        exclude = ['student']


class AnswarQuestionForm(forms.ModelForm):
    class Meta:
        model = AnswarQuestion
        exclude = ['teacher', 'question']
