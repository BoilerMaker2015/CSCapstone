"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

app_name = 'project'

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),

    #url(r'^project$', views.getProject, name='Project'),
    url(r'^project/projectForm$', views.addProject, name='ProjectForm'),    #addProject() method handle both get and post projet Form situations
    url(r'^project/submitProject$', views.addProject, name='submitProject'),
	url(r'^project/bookmarkProject$',views.bookmarkProject,name='BookmarkProject'),

]