from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    #name = forms.CharField(required=True,max_length=200)
    #description = forms.CharField(max_length=10000,required=True)

    class Meta:
        model = Project
        fields = ['title','description', 'creator', 'language', 'assigned', 'progress', 'assigned_group']

    # created_at = forms.DateTimeField('date created')
    # updated_at = forms.DateTimeField('date updated')

