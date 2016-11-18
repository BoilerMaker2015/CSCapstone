from django import forms


class ProjectForm(forms.Form):
    name = forms.CharField(required=True,max_length=200)
    description = forms.CharField(max_length=10000,required=True)
    created_at = forms.DateTimeField('date created')
    updated_at = forms.DateTimeField('date updated')

