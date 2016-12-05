"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render, redirect
from .forms import ProjectForm
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib import messages
from AuthenticationApp.models import Platform,Skill


from . import models
from .models import Project


def getProjects(request):
    # projects_list = models.Project.objects.all()
    # list = []
    projects_list = []
    # sorting by bookmark first then only list out the unbookmarked
    for i in Project.objects.all():
        if request.user in i.bookmarkMembers.all():
            projects_list.append(i)
    for i in Project.objects.all():
        if request.user not in i.bookmarkMembers.all():
            projects_list.append(i)

    return render(request, 'projects.html', {
        'projects': projects_list,
    })


def getBookMarkProjectOnly(request):
    if request.user.is_authenticated:
        project_list = Project.objects.all()
        context = {
            'projects': project_list
        }

        return render(request, 'bookmarkprojects.html', context)
    return render(request, 'autherror.html')


def getProject(request):
    if request.user.is_authenticated:
        in_id = request.GET.get('id', 'None')
        project = Project.objects.get(pk=in_id)
        context = {
            'project': project
        }

    return render(request, 'project.html', context)


def addProject(request):
    form_class = ProjectForm


    user_status = request.user.is_engineer
    if user_status == True:
        if request.method == 'POST':
            form = form_class(data=request.POST)
            print("sadssssssa")
            print("sadssssssa")
            if form.is_valid():
                # print("i am here")
                name = request.POST.get('name')
                description = request.POST.get('description')
                time = timezone.now()
                #platform = request.POST.get('project_platform')
                #print(platform)




                #print(platform)
                #print(type(platform))

                new_project = Project(name=name, description=description, created_at=time, updated_at=time)


                new_project.save()

                platform = form.cleaned_data['project_platform']
                for i in platform:
                    platform = Platform.objects.get(platform=i)
                    new_project.project_platform.add(platform)
                    new_project.save()

                return redirect('project:Projects')
        else:
            # print("asdas")

            return render(request, 'addproject.html', {
                'form': form_class
            })

    # this person is not even
    else:
        messages.error(request, "You are not an Engineer.Unable to create a project")
        # return HttpResponseRedirect(request('project:Projects'))
        return redirect('project:Projects')




def bookmarkProject(request):
    if request.user.is_authenticated():
        in_id = request.GET.get('id', 'None')
        print(in_id)
        project = Project.objects.get(pk=in_id)
        print("user has bookedmarked " + project.name)
        project.bookmarkMembers.add(request.user)
        project.save()

        # project_list = []
        # for i in Project.objects.all():
        #     if request.user in i.bookmarkMembers.all():
        #         project_list.append(i)
        # for i in Project.objects.all():
        #     if request.user not in i.bookmarkMembers.all():
        #         project_list.append(i)

        project_list = Project.objects.all()

        context = {
            'projects': project_list
        }
        #return getProjects(request)
        #return redirect(getProjects(request))
        #return redirect('project:Projects',context)
        return render(request, 'projects.html', context)
        #return render(request,'project:Projects',context)
    # should return error
    return HttpResponse("you are not login")


# return HttpResponse("Sadsa")

# unbookmarking the project
def unbookmarkProject(request):
    if request.user.is_authenticated():
        in_id = request.GET.get('id', 'None')
        #print(in_id)
        project = Project.objects.get(pk=in_id)
        print("user has unbookedmarked " + project.name)
        project.bookmarkMembers.remove(request.user)
        project.save()

        project_list = Project.objects.all()
        context = {
            'projects': project_list
        }

        return render(request, 'projects.html', context)

    # should return error
    return render(request, 'autherror.html')


# not using the joinproject for now
def joinProject(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
    # in_name = request.GET.get('name', 'None')
    # in_group = models.Group.objects.get(name__exact=in_name)
    # in_group.members.add(request.user)
    # in_group.save();
    # request.user.group_set.add(in_group)
    # request.user.save()
    # context = {
    # 	'group': in_group,
    # 	'userIsMember ': True,
    # }
    # return render(request, 'group.html', context)
    return render(request, 'autherror.html')

    user_status = request.user.is_engineer
    if user_status == True:
        if request.method == 'POST':
            form = form_class(data=request.POST)

            if form.is_valid():
                # print("i am here")
                name = request.POST.get('name')
                description = request.POST.get('description')
                time = timezone.now()

                new_project = Project(name=name, description=description, created_at=time, updated_at=time)
                new_project.save()

                return redirect('project:Projects')
        else:
            # print("asdas")

            return render(request, 'addproject.html', {
                'form': form_class
            })

    # this person is not even
    else:
        messages.error(request, "You are not an Engineer.Unable to create a project")
        # return HttpResponseRedirect(request('project:Projects'))
        return redirect('project:Projects')
