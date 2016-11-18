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
			print("asdas")
			return redirect('project:Projects')

	#this person is not even
	else:
		return redirect('project:Projects')


