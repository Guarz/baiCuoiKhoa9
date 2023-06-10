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
