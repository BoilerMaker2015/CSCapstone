from django import forms
from .models import Project
from tinymce.widgets import TinyMCE


class ProjectForm(forms.Form):
    name = forms.CharField(required=True,max_length=200)
    description = forms.CharField(max_length=10000,required=True)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    #content = forms.CharField(widget=(attrs{'cols': 80, 'rows': 30}))

    class Meta:
        model = Project
        fields = ['name','description']

    # created_at = forms.DateTimeField('date created')
    # updated_at = forms.DateTimeField('date updated')

