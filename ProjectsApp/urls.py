"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

app_name = 'project'

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    #url(r'^project$', views.getProject, name='Project'),
    url(r'^project/projectForm$', views.getProjectForm, name='ProjectForm'),
    url(r'^project/submitProject$', views.addProject, name='submitProject'),
]