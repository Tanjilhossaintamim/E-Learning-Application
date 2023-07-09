from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from App_login.models import TeacherProfile
from App_teacher.models import Articale
from .forms import ArticalForm, QuizForm

# Create your views here.


@login_required
def write_articale(request):
    form = ArticalForm()
    teacher = TeacherProfile.objects.filter(user=request.user)
    print(teacher)
    if teacher.exists():
        if teacher[0].is_fully_filled():  # i am trying to check this condition

            if request.method == 'POST':
                form = ArticalForm(request.POST, request.FILES)
                if form.is_valid():
                    article_form = form.save(commit=False)
                    article_form.author = teacher[0]
                    article_form.save()
                    messages.success(
                        request, 'Your Article Post successfully !')
                    form = ArticalForm()
                    return HttpResponseRedirect(reverse('App_student:home'))
                else:
                    messages.warning(
                        request, 'Something Wrong please try again !')
        else:
            messages.warning(request, 'Please Fill Your Profile Info First !')
            return HttpResponseRedirect(reverse('App_login:profile'))

    else:
        messages.warning(request, 'Only Teacher Will Be Post Article !')
    return render(request, 'App_teacher/post_articale.html', context={'form': form, 'heading': 'Post Article', 'btn_name': 'Post'})


@login_required
def post_quiz(request):
    form = QuizForm()
    teacher = TeacherProfile.objects.filter(user=request.user)
    if teacher.exists():
        if teacher[0].is_fully_filled():

            if request.method == 'POST':
                form = QuizForm(data=request.POST)
                if form.is_valid():
                    quiz_form = form.save(commit=False)
                    quiz_form.teacher = teacher[0]
                    quiz_form.save()
                    messages.info(request, 'Quiz Added!')
                    form = QuizForm()
                    return HttpResponseRedirect(reverse('App_student:quiz'))
        else:
            messages.warning(request, 'Please Fill Your Profile Info First !')
            return HttpResponseRedirect(reverse('App_login:profile'))

    else:
        messages.warning(request, 'Only a teacher can post a quiz!')

    return render(request, 'App_teacher/quiz_form.html', context={'form': form})


@login_required
def my_article(request):
    teacher = TeacherProfile.objects.filter(user=request.user)
    if teacher.exists():
        articles = Articale.objects.filter(author=teacher[0])
    else:
        messages.warning(request, 'You Are not Our Teacher !')

    return render(request, 'App_teacher/my_article.html', context={'articles': articles})


@login_required
def edit_article(request, pk):
    artical = Articale.objects.get(pk=pk)
    teacher = TeacherProfile.objects.filter(user=request.user)
    if teacher.exists():
        form = ArticalForm(instance=artical)
        if request.method == 'POST':
            form = ArticalForm(request.POST, request.FILES, instance=artical)
            article_form = form.save(commit=False)
            article_form.author = teacher[0]
            article_form.save()
            messages.success(request, 'Saved Successfully !')
            return HttpResponseRedirect(reverse('App_teacher:my_article'))
    else:
        messages.warning(request, 'You Are not Our Teacher !')
        return HttpResponseRedirect(reverse('App_student:home'))
    return render(request, 'App_teacher/post_articale.html', context={'form': form, 'heading': 'Edit Article', 'btn_name': 'Update'})


@login_required
def delete_article(request, pk):
    artical = Articale.objects.get(pk=pk)
    artical.delete()
    messages.info(request, 'Deleted Successfully !')
    return HttpResponseRedirect(reverse('App_teacher:my_article'))
