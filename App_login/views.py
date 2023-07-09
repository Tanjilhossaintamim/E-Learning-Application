from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, TeacherProfileForm, StudentProfileForm
from .models import StudentProfile, TeacherProfile

# Create your views here.


def user_sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully !')
            return HttpResponseRedirect(reverse('App_login:login'))

    return render(request, 'App_login/singup.html', context={'form': form})


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully Logged in !')
                return HttpResponseRedirect(reverse('App_student:home'))

    return render(request, 'App_login/login.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully !')
    return HttpResponseRedirect(reverse('App_login:login'))


@login_required
def edit_profile(request):
    student_profile = StudentProfile.objects.filter(user=request.user)
    teacher_profile = TeacherProfile.objects.filter(user=request.user)

    if student_profile.exists():
        form = StudentProfileForm(instance=student_profile[0])
        if request.method == 'POST':
            form = StudentProfileForm(
                request.POST, request.FILES, instance=student_profile[0])
        if form.is_valid():
            student_form = form.save(commit=False)
            student_form.user = request.user
            student_form.save()
            messages.success(request, 'Profile Saved Successfully !')
            form = StudentProfileForm(instance=student_profile[0])

    else:
        form = TeacherProfileForm(instance=teacher_profile[0])
        if request.method == 'POST':
            form = TeacherProfileForm(
                request.POST, request.FILES, instance=teacher_profile[0])
            if form.is_valid():
                teacher_form = form.save(commit=False)
                teacher_form.user = request.user
                teacher_form.save()
                form = TeacherProfileForm(instance=teacher_profile[0])
                messages.success(request, 'Profile Saved Successfully !')
            else:
                messages.warning(request, 'Some information is not valid !')

    return render(request, 'App_login/profile.html', context={'form': form})


@login_required
def view_profile(request):
    teacher = TeacherProfile.objects.filter(user=request.user)
    student = StudentProfile.objects.filter(user=request.user)
    dic = {}
    if teacher.exists():
        dic['teacher'] = teacher[0]
    elif student.exists():
        dic['student'] = student[0]
    else:
        messages.warning(request, 'Profile does not exists !')

    return render(request, 'App_login/view_profile.html', context=dic)


@login_required
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/password_change.html', context={'form': form})
