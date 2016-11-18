"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render
from .forms import ProjectForm

from . import models

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
	return render(request, 'project.html')

def addProject(request):
	form_class = ProjectForm
	
	return render(request,'addproject.html', {
		'form' : form_class
	})

