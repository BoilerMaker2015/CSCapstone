from django import forms
from .models import Project

class ProjectForm(forms.Form):
    name = forms.CharField(required=True,max_length=200)
    description = forms.CharField(max_length=10000,required=True)

    class Meta:
        model = Project
        fields = ['name','description']

    # created_at = forms.DateTimeField('date created')
    # updated_at = forms.DateTimeField('date updated')

