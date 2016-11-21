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
	print('I am in getProjects')
	return render(request, 'projects.html',
				  {'projects': projects_list})

def getProjectForm(request):
	form = ProjectForm
	return render(request, 'ProjectForm.html', {"form": form})

def addProject(request):
	form_class = ProjectForm

	user_status = request.user.is_teacher
	if user_status == True:
		if request.method == 'POST':
			form = form_class(data=request.POST)
			#form = form
			if form.is_valid():
				#print("i am here")
				#name = request.POST.get('name')
				#description = request.POST.get('description')
				#time = timezone.now()

				#new_project = Project(name=name,description=description,created_at=time,updated_at=time)
				#new_project.save()
				form.save()
				return redirect('ProjectApp:Projects')
		else:
			#print("asdas")
			return render(request, 'ProjectForm.html', {
				'form': form_class
			})

	#this person is not even
	else:
		return redirect('ProjectApp:Projects')


