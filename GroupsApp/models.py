"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser,Platform,Skill
from ProjectsApp.models import Project


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser)
   # group_skills = models.CharField(max_length=500,default=None,null=True,blank=True)
   # group_platforms = models.CharField(max_length=500,default=None,null=True,blank=True)
    group_skills = models.ManyToManyField(Skill)
    group_platform = models.ManyToManyField(Platform)

    project = models.ForeignKey(Project, blank=True, null=True)

    def __str__(self):
        return self.name