from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import teachers
from .models import students
from django.views.generic.edit import CreateView
from .form import InputForm

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

# def teachersCreateView(request):
#     teacher = teachers.objects.all()
#     return render(request, 'pages/Teachers_new.html', {'Students':teacher})
def Teachers_new(request):
    # context = {}
    # context['form'] = InputForm()
    # return render(request, "pages/Teachers_new.html", context)
    if request.method == "POST":
        # context = {}
        # context['form'] = InputForm()
        form = InputForm(request.POST)
        if form.is_valid():
            post = teachers()
            post.msgv = request.POST['msgv']
            post.name = request.POST['name']
            post.email = request.POST['email']
            post.phone = request.POST['phone']
            post.date = request.POST['date']
            post.gender = request.POST['gender']
            post.save()
            return render(request, 'Pages/Home.html')
    
    else: 
        form = InputForm()
        return render (request, "pages/Teachers_new.html", {'form': form})
    

    


# class TeachersCreateView(CreateView):
#     model = teachers
#     template_name = 'Teachers_new.html'
#     fields = '__all__'