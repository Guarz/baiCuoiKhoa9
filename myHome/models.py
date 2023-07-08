from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class teachers(models.Model):
    msgv = models.TextField()
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    address = models.TextField()
    ethnic = models.TextField()
    degree = models.TextField()
    
class students(models.Model):
    mssv = models.TextField()
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    gender = models.TextField()
    department = models.TextField()
    majors = models.TextField()
    classroom = models.TextField()

class CustomUser(AbstractUser):
    sex_choice = ((0, 'Nữ'), (1, 'Nam'), (2, 'Không xác định'))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice, default=0)
    address = models.CharField(default='', max_length=225)
    