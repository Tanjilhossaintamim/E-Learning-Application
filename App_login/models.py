from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError('User Must Be an Email !')
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_active', True)
        extrafields.setdefault('is_superuser', True)

        if extrafields.setdefault('is_staff') is not True:
            raise ValueError('Superuser mustbe is staff !')
        if extrafields.setdefault('is_active') is not True:
            raise ValueError('Superuser must be active !')

        if extrafields.setdefault('is_superuser') is not True:
            raise ValueError('Super user must be superuser !')

        return self.create_user(email, password, **extrafields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(
        default=False, verbose_name='Create Account As A Teacher ?')
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher_profile')
    profile_image = models.ImageField(
        upload_to='teacher_image', null=True, blank=True)
    full_name = models.CharField(max_length=20, null=True, blank=True)
    qualification = models.CharField(max_length=300, null=True, blank=True)
    subject = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(
        max_length=11, verbose_name='Phone Number', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.fields]
        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True


class StudentProfile(models.Model):
    class_6 = '6'
    class_7 = '7'
    class_8 = '8'
    class_9 = '9'
    class_10 = '10'
    class_11 = '11'
    class_12 = '12'
    class_choice = [
        (class_6, 'Six'),
        (class_7, 'Seven'),
        (class_8, 'Eight'),
        (class_9, 'Nine'),
        (class_10, 'Ten'),
        (class_11, 'Eleven'),
        (class_12, 'Twelve'),
    ]
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student_profile')
    profile_image = models.ImageField(upload_to='student_image')
    full_name = models.CharField(max_length=20, null=True, blank=True)
    your_class = models.CharField(
        max_length=2, choices=class_choice, null=True, blank=True)
    school_name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.fields]
        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True


""" create user Profile"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            TeacherProfile.objects.create(user=instance)
        else:
            StudentProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def saved_profile(sender, instance, **kwargs):
    if instance.is_teacher:
        instance.teacher_profile.save()
    else:
        instance.student_profile.save()
