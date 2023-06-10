from django.shortcuts import render
from django.http import HttpResponse
from .models import teachers
from .models import students

def index(request):
   return render(request, 'Pages/Home.html')

def contact(request):
    return render(request, 'Pages/Contact.html')

def error(request):
    return render(request, 'Pages/Error.html')

# def teachers(request):
#     return render(request, 'Pages/Home.html')

# def students(request):
#     return render(request, 'Pages/Students.html')
# Create your views here.

def list(request):
    Data = {'teachers': teachers.objects.all().order_by('-date')}
    return render(request, 'Pages/Home.html', Data)

def list_student(request):
    Data1 = {'students': students.objects.all()}
    return render(request, 'Pages/Students.html', Data1)

def list_id(request, id):
    Teachers = teachers.objects.get(id=id)
    return render(request, 'pages/Detail.html', {'Teachers':Teachers})

def list_id_student(request, id):
    Students = students.objects.get(id=id)
    return render(request, 'pages/detailStudent.html', {'Students':Students})

