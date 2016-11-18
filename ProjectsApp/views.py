"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render,redirect
from .forms import ProjectForm
from django.utils import timezone

from . import models
from .models import Project

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
	return render(request, 'project.html')

def addProject(request):
	form_class = ProjectForm

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

	return render(request,'addproject.html', {
		'form' : form_class
	})

