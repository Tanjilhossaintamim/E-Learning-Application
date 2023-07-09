from django.db import models
from App_login.models import TeacherProfile
from django.conf import settings
# Create your models here.


class Articale(models.Model):
    author = models.ForeignKey(
        TeacherProfile, on_delete=models.CASCADE, related_name='writer')
    image = models.ImageField(upload_to='article_image', null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    quiz_question = models.CharField(max_length=300)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_ans = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz_question


class QuizAnswar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='user_ans')
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='quizes')

    def __str__(self):
        return self.quiz.quiz_question
