"""
CompaniesApp URL Configuration

Created by Harris Christiansen on 10/02/2016.
"""
from django.conf.urls import url

from . import views

app_name = 'CSCap'

urlpatterns = [
    # url(r'^$', views.getIndex, name='Index'),
url(r'^$', views.getWelcome, name='Index'),
    url(r'^table$', views.getTable, name='Table'),
    url(r'^form$', views.getForm, name='Form'),
    url(r'^welcome$',views.getWelcome,name='Welcome'),
]