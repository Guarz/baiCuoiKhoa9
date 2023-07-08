from django.contrib import admin
from .models import teachers
from .models import students
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class teachersAdmin(admin.ModelAdmin):
    list_display = ['msgv', 'name', 'degree']
    list_filter = ['msgv']
    search_fields = ['msgv']
admin.site.register(teachers, teachersAdmin)

class studentsAdmin(admin.ModelAdmin):
    list_display = ['mssv', 'name', 'majors']
    list_filter = ['mssv']
    search_fields = ['mssv']
admin.site.register(students, studentsAdmin)    

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser)