"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render,redirect
from django.contrib import messages
from . import models
from . import forms
import re
from AuthenticationApp.models import MyUser,Student,Professor,Engineer

def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        context = {
            'groups' : groups_list,
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)

        plat = str(in_group.group_platforms)
        plat = plat.split(",")
        student_platforms_list = []
        for i in plat:
            student_platforms_list.append(i)

        context = {
            'group' : in_group,
            'userIsMember': is_member,
            #'student_skills_list' : student_skills_list,
            #'student_platforms_list' : student_platforms_list,
        }
        return render(request, 'group.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

# creating group
def getGroupForm(request):
    if request.user.is_authenticated():
        if request.user.is_student:
            return render(request, 'groupform.html')
        else:
            messages.error(request, "You are not a Student.Unable to create a group")
            return redirect('group:Groups')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.GroupForm(request.POST)
            if form.is_valid():
                if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'groupform.html', {'error' : 'Error: That Group name already exists!'})
                new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
                new_group.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'groupformsuccess.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

# only students can join group
def joinGroup(request):
    if request.user.is_authenticated():
        if request.user.is_student:
            in_name = request.GET.get('name', 'None')
            in_group = models.Group.objects.get(name__exact=in_name)
            in_group.members.add(request.user)
            in_group.save();
            #request.user.group_set.add(in_group)
            #request.user.save()
            updateGroup(in_group)
            context = {
                'group' : in_group,
                'userIsMember': True,
            }
            return render(request, 'group.html', context)
        else:
            messages.error(request,"You are not a Student.Unable to join group")
            return redirect('group:Groups')
    return render(request, 'autherror.html')
    
def unjoinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        #updateGroup(in_group)
        in_group.members.remove(request.user)
        in_group.save();
        request.user.group_set.remove(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': False,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')


def updateGroup(group):
    # student_list = in_group.members.all()
    # user_objects = MyUser.objects.filter(id__in=[user.id for ])
    user_list = []
    # converting those users into a list first instead of the default Queryset object from django
    for i in group.members.all():
        user_list.append(i)

    student_list = []
    for i in user_list:
        stud = Student.objects.get(user=i)
        student_list.append(stud)

    # appending the student skills
    # hashset_skills = {}
    hashset_skills = set()
    student_skills_list = []
    for student in student_list:
        if student.skills not in hashset_skills:
            hashset_skills.add(student.skills)
            student_skills_list.append(student.skills)

    print(student_skills_list)

    # hashset_platform = {}
    hashset_platform = set()
    student_platform_list = []
    pattern = re.compile('([^\s\w]|_)+')

    for student in student_list:
        # print(type(student.platforms))
        # s = student.platforms[1:student.platforms.length]
        s = student.platforms
        s = s.split(",")
        for i in s:
            i = pattern.sub('', i)
            i = i.lstrip()
            # print(i)
            if i not in hashset_platform:
                hashset_platform.add(i)


    for student in student_list:
        # print(type(student.platforms))
        # s = student.platforms[1:student.platforms.length]
        s = student.platforms
        s = s.split(",")
        for i in s:
            i = pattern.sub('', i)
            i = i.lstrip()
            # print(i)
            if i not in hashset_platform:
                hashset_platform.add(i)
                student_platform_list.append(i)
                if group.group_platforms == None:
                    group.group_platforms = i + ","
                else:
                    group.group_platforms = str(group.group_platforms) + i + ","


    group.save()