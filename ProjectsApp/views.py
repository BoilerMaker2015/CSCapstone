"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render,redirect
from .forms import ProjectForm
from django.utils import timezone

from . import models
from .models import Project
from .forms import ProjectForm
def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html',
				  {'projects': projects_list})


# when user get projectForm, it will go to request.method else branch. when user submit the project Form, it will go to request.method the first branch.
def addProject(request):
	form_class = ProjectForm

	#user_status = request.user.is_engineer
	#if user_status == True:

	if request.method == 'POST':   #when user submit the project Form
		form = form_class(data=request.POST)
		if form.is_valid():

			form.save()
			return redirect('project:Projects')

	else:  # when user want to get the project Form

		return render(request, 'ProjectForm.html', {
			'form': form_class
		})

	#this person is not even
	#else:
		#return redirect('ProjectApp:Projects')


