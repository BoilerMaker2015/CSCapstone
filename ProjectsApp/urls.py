"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

app_name = 'project'

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    url(r'^project$', views.getProject, name='Project'),
    url(r'^addproject$', views.addProject, name='AddProject'),
]