"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

app_name = 'group'

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='Groups'),
    # this goes to the page to create a group
	url(r'^group/form$', views.getGroupForm, name='GroupForm'),
    url(r'^group/formsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
    url(r'^group/join$', views.joinGroup, name='GJoin'),
    url(r'^group/unjoin$', views.unjoinGroup, name='GUnjoin'),
    url(r'^group$', views.getGroup, name='Group'),
    url(r'^group/platform$', views.GPlatform, name='GPlatform'),
    url(r'^group/skill$', views.GSkill, name='GSkill'),
    url(r'^group/recommend$', views.recommendProject, name='Recommend'),
]