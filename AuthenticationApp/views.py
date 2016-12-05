"""AuthenticationApp Views
Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from django.core.urlresolvers import reverse

from .forms import LoginForm, RegisterForm, UpdateForm, UpdateStudentForm, UpdateProfessorForm, UpdateEngineerForm

from .models import MyUser, Student, Professor, Engineer,Platform,Skill
from CompaniesApp.models import Company




# Auth Views

def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if next_url is None:
        next_url = "body.html"
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Success! Welcome, ' + (user.first_name or ""))
            login(request, user)
            '''
            if request.user.is_professor:
                # redirect to teacher index
                return HttpResponseRedirect(reverse('TeacherApp:index'))
            '''

            return render(request, 'body.html')      
           

            
        else:
            messages.warning(request, 'Invalid username or password.')

    context = {
        "form": form,
        "page_name": "Login",
        "button_value": "Login",
        "links": ["register"],
    }
    return render(request, 'auth_form.html', context)


def auth_logout(request):
    logout(request)
    messages.success(request, 'Success, you are now logged out')
    return render(request, 'body.html')


def auth_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        new_user = MyUser.objects.create_user(email=form.cleaned_data['email'],
                                              password=form.cleaned_data["password2"],
                                              first_name=form.cleaned_data['firstname'],
                                              last_name=form.cleaned_data['lastname'])
        choice = form.cleaned_data['choice']
        #print('you selected' + choice)
        new_user.save()


        # Registering either student teacher or engineer
        if choice == 'Student':
            #setting the user attirubte to be as a student
            new_user.is_student = True
            new_user.save()
            #creating the student object with the default attributes, put it as NONE first as you need to initialise it
            new_student = Student(user=new_user,major=None)
            new_student.save()
        elif choice == 'Professor':
            new_user.is_professor = True
            new_user.save()

            new_professor = Professor(user=new_user, university = None, phone = None) # note: maybe we do not need to give the special attributes, since it is null : true.)
            new_professor.save()
        elif choice == 'Engineer':
            new_user.is_engineer = True
            new_user.save()

            new_engineer = Engineer(user=new_user, company = None, position = None, phone = None)
            new_engineer.save()

        login(request, new_user);
        messages.success(request, 'Success! Your account was created.')
        return render(request, 'body.html')

    context = {
        "form": form,
        "page_name": "Register",
        "button_value": "Register",
        "links": ["login"],
    }
    return render(request, 'auth_form.html', context)


@login_required
def update_profile(request):
    form = UpdateForm(request.POST or None, instance=request.user)
    # form_2_student = UpdateStudentForm(request.POST or None, instance=request.user)
    if request.user.is_student:
        form_2 =UpdateStudentForm(request.POST or None, instance=request.user.student)
    elif request.user.is_professor:
        form_2 =UpdateProfessorForm(request.POST or None, instance=request.user.professor)
    elif request.user.is_engineer:
        form_2 =UpdateEngineerForm(request.POST or None, instance=request.user.engineer)   
    else:
        form_2 = None



    # print(request.user.student.pk)
    #print(request.user.student.year)


    if request.user.is_student:
        form_2 = UpdateStudentForm(request.POST or None, instance = request.user.student)
        if form.is_valid() and form_2.is_valid():
            #print("the pk of the user is " + request.user.id)
            # have to get the child object of the user first (either "Student" / "professor" or "enginneer")
            #print(form_2.cleaned_data['testing'])
            student = request.user.student
            student.major = form_2.cleaned_data['major']

            student.platform.clear()
            student.save()
            for i in form_2.cleaned_data['platform']:
                #plat = Platform(platform=i)
                #plat.save()

                plat = Platform.objects.get(platform=i)

               # print(type(platform))
                #print(type(i))

                #platform.save()

                student.platform.add(plat)
                student.save()

            for i in form_2.cleaned_data['skill']:
                #skill = Skill(skill=i)
                #skill.save()
                student.skill.add(i)
                student.save()



            #platform = Platform(platform=form_2.cleaned_data[''])


            #Skill = form_2.cleaned_data['skills']
           # student.skills = form_2.cleaned_data['skills']
           # student.platforms = form_2.cleaned_data['platforms']
            #print(form_2.cleaned_data['platforms'])

            student.year = form_2.cleaned_data['year']

            #color = form_2.cleaned_data['favorite_colors']



            student.save()
            form.save()
            #form_2.save()

            messages.success(request, 'Success, your profile was saved!')

    elif request.user.is_professor:

        if form.is_valid() and form_2.is_valid():

            professor = request.user.professor
            professor.university = form_2.cleaned_data['university']
            professor.teachClass.create(title = form_2.cleaned_data['teachClass'])
            professor.phone = form_2.cleaned_data['phone']
            form.save()
            professor.save()
            messages.success(request, 'Success, your profile was saved!')
            messages.success(request, 'you are a professor')
            return HttpResponseRedirect(reverse('TeacherApp:index'))

    elif request.user.is_engineer:

        if form.is_valid() and form_2.is_valid():
            engineer = request.user.engineer
            company = Company.objects.get(pk=form_2.cleaned_data['company'].id)
            company.members.add(request.user)
            #engineer.company = form_2.cleaned_data['company']

            engineer.position = form_2.cleaned_data['position']
            engineer.phone = form_2.cleaned_data['phone']
            form.save()
            form_2.save()
            engineer.save()
            messages.success(request, 'Success, your profile was saved!')

    else:

        if form.is_valid():
            form.save()
            messages.success(request, 'Success, your profile was saved!')



    context = {
        "form": form,
        "form_2": form_2,
        "page_name": "Update",
        "button_value": "Update",
        "links": ["logout"],
    }
    return render(request, 'auth_form.html', context)