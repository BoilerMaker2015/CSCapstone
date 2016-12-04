
from django.shortcuts import render
from . import models
from django.contrib import messages
from . import forms
# Create your views here.
def index(request) :
    teachers_list = models.Teacher.objects.all()
    context = {
        'teachers': teachers_list,
    }
    messages.success(request, 'In teacher Index method')
    return render(request, 'teacherIndex.html', context)

def getTeacherForm(request):
    return render(request, 'teacherForm.html')

def submitTeacher(request):
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        if form.is_valid():
            new_teacher = models.Teacher()
            new_teacher.first_name = form.cleaned_data['first_name']
            new_teacher.last_name = form.cleaned_data['last_name']
            new_teacher.university = form.cleaned_data['university']
            new_teacher.phone = form.cleaned_data['phone']
            new_teacher.save()
            teachers_list = models.Teacher.objects.all()
            print("first_name" + new_teacher.first_name + ", last_name : " + new_teacher.last_name)
            print("teatcher_list[0]: " + teachers_list[0].first_name)
            print("teatcher_list[1]: " + teachers_list[1].first_name)

            context = {
                'teachers' : teachers_list,
            }
            return render(request, 'teacher.html', context)
        else:
            form = forms.TeacherForm()
    return render(request, 'teacher.html')

def teachClass(request):

    class_list = request.user.professor.teachClass.all()
    context = {
    'classList': class_list,
    }
    
    messages.success(request, 'In teacher teachClass method')
    return render(request, 'teachClass.html', context)

 

def classForm(request):
    if request.method == 'POST':
        form = forms.TeachClassForm(request.POST)
        if form.is_valid():
            new_class = models.TeachClass()
            new_class.title = form.cleaned_data['title']
            new_class.save()
            class_list = request.user.teachClass.object.all()
            context = {
            'classList': class_list,
            }
            messages.success(request, 'In teacher classForm method')
            return render(request, 'classForm.html', context)

    else:

          # when the request method is get
          # do nothing
    

        class_list = request.user.professor.teachClass.all()
        context = {
        'classList': class_list,
        }
        messages.success(request, 'In teacher classForm method')
        return render(request, 'classForm.html', context)

