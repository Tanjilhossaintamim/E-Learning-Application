from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, TeacherProfile, StudentProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'is_teacher']


class TeacherProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TeacherProfile
        fields = ['profile_image', 'full_name', 'qualification',
                  'subject', 'date_of_birth', 'phone_no']


class StudentProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = StudentProfile
        fields = ['profile_image', 'full_name', 'your_class',
                  'school_name', 'phone_no', 'date_of_birth']
