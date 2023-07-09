from django.db import models
from App_login.models import StudentProfile, TeacherProfile
# Create your models here.


class AskedQuestion(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.subject
    
class AnswarQuestion(models.Model):
    teacher=models.ForeignKey(TeacherProfile,on_delete=models.CASCADE)
    question=models.ForeignKey(AskedQuestion,on_delete=models.CASCADE)
    answar=models.TextField()
