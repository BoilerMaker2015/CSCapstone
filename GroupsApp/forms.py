"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms
from tinymce.widgets import TinyMCE

class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)

class CommentForm(forms.Form):
    comment = forms.CharField(widget=TinyMCE,required=False,label='Type Your Comment Here')