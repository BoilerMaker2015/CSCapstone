
from django.shortcuts import render,redirect, HttpResponse
from . import models
from django.contrib import messages
from . import forms
from AuthenticationApp.models import Student,MyUser
from django.core.urlresolvers import reverse 
from django.http import HttpResponseRedirect

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
    if request.user.is_authenticated:
        if request.user.is_professor:
            class_list = request.user.professor.teachClass.all()
          
            context = {
            'classList': class_list,
            }
            
            messages.success(request, 'In teacher teachClass method')
            return render(request, 'teachClass.html', context)
        else:
            messages.error(request,"You are not a teacher")
            return render(request,'body.html')
    return HttpResponse("please log in")


 
#classForm post method does not work and deal with it later
def classForm(request):
    '''
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
    '''
          # when the request method is get
          # do nothing
    

    class_list = request.user.professor.teachClass.all()
    context = {
    'classList': class_list,
    }
    messages.success(request, 'In teacher classForm method')
    return render(request, 'classForm.html', context)

def viewStudents(request):

    class_id = request.GET.get('id')
    myclass = models.TeachClass.objects.get(pk=class_id)
    student_list= myclass.students.all
    context = {
        'studentList': student_list,
        'class_id': class_id,
    } 
    return render(request, 'students.html', context)

def removeStudent(request, classId, studentId):

    #student_id = request.GET.get('studentId')
    #class_id = request.GET.get('classId')
    print("studuentId" + studentId)
    print("studuentId" + classId)
    student = Student.objects.get(pk=studentId)
    myclass = models.TeachClass.objects.get(pk=classId)
 
    myclass.students.remove(student)
    #url = reverse('TeacherApp:viewStudents', kwargs={'id': classId})
    #return HttpResponseRedirect(reverse(url))
    #return HttpResponseRedirect(reverse('/class/?id=%s/' % classId))
    #return redirect('TeacherApp:viewStudents', kwargs={'id': classId})
    
    student_list= myclass.students.all
    context = {
        'studentList': student_list,
        'class_id': classId,
    } 
    return render(request, 'students.html', context) 

def addStudent(request, classId):
    if request.method == 'GET':
        context = {
            'class_id': classId,
        } 
        return render(request, "addStudent.html", context)

    else:

        form = forms.EmailForm(request.POST)
        if form.is_valid():
           
            email = form.cleaned_data['email']
            
            myUser = MyUser.objects.get(email=email)
        
            #student = Student.objects.filter(user=myUser)[0]
            student = myUser.student  #the above method also works
      
            myclass = models.TeachClass.objects.get(pk=classId)
         
            myclass.students.add(student)
      
            student_list= myclass.students.all
            context = {
                'studentList': student_list,
                'class_id': classId,
            } 
            return render(request, 'students.html', context) 

def addClass(request):
    if request.method == 'GET':
     
        return render(request, "addClass.html")
    else:
        form = forms.ClassForm(request.POST)
        if form.is_valid():
           
            if request.user.is_professor:
                new_class = models.TeachClass()
                new_class.title = form.cleaned_data['title']
                print("title" + new_class.title )
                new_class.save()
                request.user.professor.teachClass.add(new_class)
                class_list = request.user.professor.teachClass.all()
                context = {
                    'classList': class_list,
                    'user': request.user,
                }
                #messages.success(request, 'In teacher add class method')
                return render(request, 'teachClass.html', context)

            else:
                messages.success(request, 'you are not a professor')
                class_list = models.TeachClass.all()
                context = {
                    'classList': class_list,
                    'user': request.user,
                }
                #messages.success(request, 'In teacher add class method')
                return render(request, 'teachClass.html', context)

      




            
