from django.conf.urls import url
from . import views

app_name='engineer'

urlpatterns=[
    url(r'^engineer/index$', views.index, name="index"),  # define the homepage for engineerapp
    url(r'^engineerForm', views.addEngineer, name='EngineerForm'),


]