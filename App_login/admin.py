from django.contrib import admin
from .models import User, TeacherProfile, StudentProfile
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''

    list_display = ('id', 'email')
    list_per_page = 10


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    '''Admin View for TeacherProfile'''

    list_display = ('id', 'full_name', 'qualification',
                    'subject', 'phone_no', 'profile_image', 'join_date')
    list_per_page = 10


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    '''Admin View for StudentProfile'''

    list_display = ('id', 'full_name', 'your_class', 'school_name',
                    'phone_no', 'date_of_birth', 'join_date', 'profile_image')
    list_per_page = 10
