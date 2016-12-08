"""
CompaniesApp Models

Created by Jacob Dunbar on 10/2/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser

# Create your models here.

    
    def __str__(self):
        return self.name
