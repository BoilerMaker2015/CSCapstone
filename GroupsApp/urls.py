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
    url(r'^group/(?P<group_name>\w+)$', views.getGroup, name='Group'),
    url(r'^group/(?P<groupId>\d+)/project/(?P<projectId>\d+)', views.applyProject, name = 'ApplyProject'), 
    
  
    url(r'^group/platform$', views.GPlatform, name='GPlatform'),
    # url(r'^group/skill$', views.GSkill, name='GSkill'),
    url(r'^group/recommend$', views.recommendProject, name='Recommend'),
    url(r'^group/comments/(?P<group_id>\d+)$', views.comments, name='Comments'),
    url(r'^group/addComment/(?P<group_id>\d+)$',views.addComment,name='AddComment'),
    url(r'^group/viewAllProject$',views.showAllProject,name="ViewAllProject"),
    url(r'^group/addMember/(?P<group_id>[0-9]+)$',views.addMember,name='AddMember'),
    url(r'^addSubComment/(?P<comment_id>[0-9]+)/$', views.addSubComment, name='addSubComment'),
    #url(r'^group$', views.getGroup, name='Group'),


]

