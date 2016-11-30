"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from EngineerApp.models import Engineer
class Project(models.Model):

    
    #user = models.ForeignKey(MyUser, default=1)  # same as below
  
    members = models.ManyToManyField(MyUser)  
    #bookmark = models.ManyToManyField(MyUser)
    name = models.CharField(max_length=200)  #which is the project title

    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    
   
    creator = models.ForeignKey(Engineer, default=1)
    language = models.CharField(max_length = 200, null= True)
    assigned = models.BooleanField(default = False)
    progress = models.CharField(max_length = 200, default= "none")
    assigned_group =  models.CharField(max_length = 100, default = "none")



    # TODO Task 3.5: Add field for company relationship
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)

    def __str__(self):
        return self.title + ", creator" + str(self.creator) + ", progress" + self.progress