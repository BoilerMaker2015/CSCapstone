"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from EngineerApp.models import Engineer
class Project(models.Model):
    '''
    user = models.ForeignKey(MyUser, default=1)
    name = models.CharField(max_length=200)  #which is the project title
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    '''
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length=10000)
    creator = models.ForeignKey(Engineer, default=1)
    language = models.CharField(max_length = 200, null= True)
    assigned = models.BooleanField(default = False)
    progress = models.CharField(max_length = 200, default= "none")
    assigned_group =  models.CharField(max_length = 100, default = "none")


    def __str__(self):
        return self.title + ", creator" + str(self.creator) + ", progress" + self.progress