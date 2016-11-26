"""AuthenticationApp Views
Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from .forms import LoginForm, RegisterForm, UpdateForm, UpdateStudentForm
from .models import MyUser, Student, Professor, Engineer


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
            new_student = Student(user=new_user,major=None,skills=None)
            new_student.save()
        elif choice == 'Professor':
            new_user.is_professor = True
            new_user.save()

            new_professor = Professor(user=new_user)
            new_professor.save()
        elif choice == 'Engineer':
            new_user.is_engineer = True
            new_user.save()

            new_engineer = Engineer(user=new_user)
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
    else:
        form_2 = None



    # print(request.user.student.pk)
    if request.user.is_student:
        form_2 = UpdateStudentForm(request.POST or None, instance = request.user.student)
        if form.is_valid() and form_2.is_valid():
            #print("the pk of the user is " + request.user.id)
            # have to get the child object of the user first (either "Student" / "professor" or "enginneer")
            student = request.user.student
            student.major = form_2.cleaned_data['major']
            student.skills = form_2.cleaned_data['skills']
            student.save()
            form.save()
            #form_2.save()

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