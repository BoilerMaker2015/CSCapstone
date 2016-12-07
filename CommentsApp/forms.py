
from django import forms
from .models import Comment
class CommentForm(forms.Form):
    comment = forms.CharField(max_length=500)
    class Meta:
        model = Comment
        fields = ['comment']



