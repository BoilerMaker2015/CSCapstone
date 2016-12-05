"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser,Platform,Skill
from CompaniesApp.models import Company

class Project(models.Model):
    bookmarkMembers = models.ManyToManyField(MyUser)

    #bookmark = models.ManyToManyField(MyUser)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')


    # TODO Task 3.5: Add field for company relationship
    #company = models.ForeignKey(Company)

    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)
    project_platform = models.ManyToManyField(Platform)
    project_skill = models.ManyToManyField(Skill)
    

    def __str__(self):
        return self.name