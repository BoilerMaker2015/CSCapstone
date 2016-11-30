"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render,redirect
from .forms import ProjectForm
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib import messages


from . import models
from .models import Project
from .forms import ProjectForm
# when user get projectForm, it will go to request.method else branch. when user submit the project Form, it will go to request.method the first branch.

def getProjects(request):
	projects_list = models.Project.objects.all()

	return render(request, 'projects.html', {
        'projects': projects_list,
    })


def addProject(request):
	form_class = ProjectForm

	#user_status = request.user.is_engineer
	#if user_status == True:

	if request.method == 'POST':   #when user submit the project Form
		form = form_class(data=request.POST)
		if form.is_valid():

            
			#form.save()
			#return redirect('project:Projects')

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

def bookmarkProject(request):
	# if request.user.is_authenticated():
	# 	in_name = request.GET.get('name', 'None')
	# 	is_bookmarked = models.Project.objects.get(name__exact=in_name)
	# 	is_bookmarked.bookmark.add(request.user)
	# 	# is_bookmarked.save()
	# 	request.user.group_set.add(is_bookmarked)
	# 	# request.user.save()
	# 	context = {
	# 		'bookmark' : is_bookmarked,
	# 		'projectIsBookMark' : True,
	# 	}
	# 	#return render(request,'projects.html',context)
	return HttpResponse("Sadsa")





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
				#print("i am here")
				name = request.POST.get('name')
				description = request.POST.get('description')
				time = timezone.now()
				new_project = Project(name=name,description=description,created_at=time,updated_at=time)
				new_project.save()
				return redirect('project:Projects')
		else:
			#print("asdas")

			return render(request, 'addproject.html', {
				'form': form_class
			})

	#this person is not even
	else:
		messages.error(request, "You are not an Engineer.Unable to create a project")
		#return HttpResponseRedirect(request('project:Projects'))
		return redirect('project:Projects')


