"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from . import models
from . import forms
from CommentsApp.models import Comment
from CommentsApp.forms import CommentForm
from ProjectsApp.models import Project
from AuthenticationApp.models import MyUser,Student,Professor,Engineer
from ProjectsApp.models import Project
from django.shortcuts import redirect
from django.urls import reverse
from TeacherApp.forms import EmailForm
def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        context = {
            'groups' : groups_list,
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def compare_group_project(group,project_id):
    required_skill_list = []
    required_platform_list = []
    project = Project.objects.get(pk=project_id)
    group_platform_list = []
    group_skill_list = []
    #print(group.name)
    for required_skill in project.project_skill.all():
        required_skill_list.append(required_skill.skill)
    for required_platform in project.project_platform.all():
        required_platform_list.append(required_platform.platform)
    #print("project name is " + str(project.id))
    #print( "the proejct skills " + str(project.project_skill.all()))

    #print("required skill list is " + str(required_skill_list))
    #print("requiredp latform list is " + str(required_platform_list))
        #group_skill_list.append(group_skill.skill)

    for group_platform in group.group_platform.all():
        group_platform_list.append(group_platform.platform)
    for group_skill in group.group_skills.all():
        group_skill_list.append(group_skill.skill)

    # for skill in group_skill_list:
    #     if skill not in required_skill_list:
    #         print("sadsadsa")
    #         return False
    for skill in required_skill_list:
        if skill not in group_skill_list:
            print("asdsa")
            return False

    for platform in required_platform_list:
        if platform not in group_platform_list:
            print(platform)
            #print("asdsadsadsadasdsadsa")
            return False

    # for group_platform in group.group_platform.all():
    #     if group_platform.platform not in required_platform_list:
    #         print("the false is " + group_platform.platform)
    #         print('sa')
    #         return False
    # for group_skill in group.group_skills.all():
    #     if group_skill.skill not in required_skill_list:
    #         print("ww")
    #         return False

    #
    # for matched_skill in group.group_skills.all():
    #     if matched_skill not in project.project_skill.all():
    #         return False
    # for matched_platform in group.group_platform.all():
    #     if matched_platform not in project.project_platform.all():
    #         return False
    return True


def showAllProject(request):
    #projects_list = []
    # sorting by bookmark first then only list out the unbookmarked
    if request.user.is_authenticated:
        projects_list = Project.objects.all()

        return render(request, 'projects.html', {
            'projects': projects_list,
        })
    else:
        return render(request,'autherror.html')


def recommendProject(request):
    if request.user.is_authenticated():

        id = request.GET.get('id','None')
        print(id)
        #print("asdsa")

        current_group = models.Group.objects.get(pk=id)
        #compare_group_project(current_group,Project.objects.get(name='wakao'))

        #print(Project.objects.all())
        project_all = Project.objects.all()
        matched_project_list = []

        for project in Project.objects.all():
            project_id = project.id
            if compare_group_project(current_group,project_id):
                matched_project_list.append(project)

        # print("the recommended projects are")
        # for i in matched_project_list:
        #     print(i)


        #this_group = models.Group.objects.get(pk=)
        # groups_list = models.Group.objects.all()
        # context = {
        #     'groups': groups_list,
        # }
        # return render(request, 'groups.html', context)
        print(matched_project_list)
        context ={
            'projects': matched_project_list,
            'groupId' : id
        }
        return  render(request, "recommendProjects.html", context)
        
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        #print(in_name)
        #print(group_name)
        #in_group = models.Group.objects.get(name=group_name)
        in_group = models.Group.objects.get(name=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)

       # plat = str(in_group.group_platforms)
       #  plat = plat.split(",")
       #  student_platforms_list = []
       #  for i in plat:
       #      student_platforms_list.append(i)
        student_skills_list = []
        student_platforms_list = []
        for i in in_group.group_skills.all():
            student_skills_list.append(i)
        for i in in_group.group_platform.all():
            student_platforms_list.append(i)

        if in_group.project == None:
            project_name = None
        else:
            project_name = in_group.project.name

        context = {
            'group' : in_group,
            'project_id' : in_group.id,
            'userIsMember': is_member,
            'student_skills_list' : student_skills_list,
            'student_platforms_list' : student_platforms_list,
            'project_applied': project_name,
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

                new_group.members.add(request.user)
                new_group.save()
                update_group(new_group)
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

            update_group(in_group)
            student = request.user.student
            print(student.skill.all())

            if in_group.project == None:
                project_name = None
            else:
                project_name = in_group.project.name

            #request.user.group_set.add(in_group)
            #request.user.save()
            #updateGroup(in_group)
            context = {
                'group' : in_group,
                'userIsMember': True,
                'project_applied' : project_name,
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
        update_group(in_group)
        in_group.save()
        request.user.group_set.remove(in_group)
        request.user.save()
        if in_group.project == None:
            project_name = None
        else:
            project_name = in_group.project.name

        context = {
            'group' : in_group,
            'userIsMember': False,
            'project_applied': project_name,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')

def GPlatform(request):
    in_name = request.GET.get('name', 'None')
    in_group = models.Group.objects.get(name__exact=in_name)
    context = {
        'group' : in_group,
        'userIsMember': False,
    }
    return render(request, 'platform.html', context)

def GSkill(request):
    in_name = request.GET.get('name', 'None')
    in_group = models.Group.objects.get(name__exact=in_name)
    context = {
        'group' : in_group,
        'userIsMember': False,
    }
    return render(request, 'skill.html', context)


def update_group(group):
    group.group_skills.clear()
    group.group_platform.clear()
    group.save()
    print("aiite")
    student_list = []
    for member in group.members.all():
        student_list.append(member.student)
    #student_list = group.members.all()
    for student in student_list:
        for skill_object in student.skill.all():
            # print(type(skill_object))
            group.group_skills.add(skill_object)
        for platform_object in student.platform.all():
            group.group_platform.add(platform_object)
    group.save()



def applyProject(request, groupId, projectId):
    
    project = Project.objects.get(pk=projectId)
    group = models.Group.objects.get(pk=groupId)
    group.project = project
    print("project desctip:" + group.project.description)
    group.save()
    # matched_project_list = 
    # context ={
    #     'projects': matched_project_list,
    #     'groupId' : id
    # }
    print("goroup project:" + group.project.name)
    
    
    in_group = models.Group.objects.get(pk=groupId)
    is_member = in_group.members.filter(email__exact=request.user.email)
    recommended_project_applied = in_group.project.name


    context = {
        'group' : in_group,
        'userIsMember': is_member,
        'project_applied' : recommended_project_applied,
    }
    #return HttpResponse("asdsadsas")
    return render(request,'group.html',context)
    #return redirect('group:Group',context)
    #return redirect('group:G')

def comments(request, group_id):

    if request.user.is_authenticated:
        in_group = models.Group.objects.get(pk=group_id)
        comments = in_group.comments.all()
        # name = in_group.project.name
       # name = in_group.project_id
        if in_group.project == None:
            project_name = None
        else :
            project_name = in_group.project.name

        print(in_group)
        #userIsMember = in_group.objects.filter()
        is_member = in_group.members.filter(email__exact=request.user.email).exists()
        print(is_member)
        context = {
            'group' : in_group,
            'userIsMember': is_member,
            'project_applied' : project_name,
            'comments': comments,
           
        }
        return render(request,'groupComments.html',context)


    else:

        return render(request, 'autherror.html')



# submit a comment
def addComment(request,group_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            in_group = models.Group.objects.get(pk=group_id)
            content = request.POST['comment']
            new_comment = Comment()
            new_comment.comment = content
            new_comment.creator = request.user
            new_comment.save()
            in_group.comments.add(new_comment)
           

        return redirect(reverse("group:Comments", args=[group_id]))
       
            
    else:

        return render(request, 'autherror.html')



def deleteGroup(request):
    if request.user.is_authenticated:
        in_name = request.GET.get('name',None)
        in_group = models.Group.objects.get(name=in_name)
        if request.user not in in_group.members.all():
            return HttpResponse("NICE TRY PUNK")
        in_group.delete()
        groups_list = models.Group.objects.all()
        context = {
            'groups': groups_list,
        }
        messages.success(request,"You have successfully deleted the group")
        return render(request, 'groups.html', context)
    else:
        return render(request, 'autherror.html')




def addMember(request, group_id):

    if request.method == 'GET':
        print("aiite")
        return render(request, 'autherror.html')

    if request.method=='POST':
        in_group = models.Group.objects.get(pk=group_id)
        form = EmailForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            myUser = MyUser.objects.get(email=email)
            if myUser != None and myUser.student:
                in_group.members.add(myUser)
            else:
                messages.error(request, 'the email is not valid')
            return redirect(reverse('group:Group', args=[in_group.name]))

        else:
            messages.error(request, "the form is not valid")
            return redirect(reverse('group:Group', args=[in_group.name]))
    else:
        return render(request, 'autherror.html')

