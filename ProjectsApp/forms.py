from django import forms
from .models import Project
from tinymce.widgets import TinyMCE
from AuthenticationApp.models import Platform, Skill


class ProjectForm(forms.Form):
    name = forms.CharField(required=True,max_length=200)
    #description = forms.CharField(max_length=10000,required=True)
    description = forms.CharField(widget=TinyMCE,required=False,label='description')
    #content = forms.CharField(widget=(attrs{'cols': 80, 'rows': 30}))
    platform_choice = []
    counter = 0

    for i in Platform.objects.all():
        choice = (i.platform,i.platform)
        platform_choice.insert(counter,choice)
        counter = counter + 1

    counter = 0
    skill_choice = []
    for j in Skill.objects.all():
        skill = (j.skill,j.skill)
        skill_choice.insert(counter,skill)
        counter = counter + 1




    # platform_choice = [
    #     ('IOS Programming', 'IOS Programming'),
    #     ('Android Programming', 'Android Programming'),
    #     ('Web Development', 'Web Development'),
    # ]


    # skill_choice = (
    #     ('C++', 'C++'),
    #     ('Java', 'Java'),
    #     ('Python', 'Python'),
    # )

    #project_platform = forms.ChoiceField(required=False)
    project_platform = forms.MultipleChoiceField(label="Platform", choices=platform_choice,
                                          widget=forms.CheckboxSelectMultiple,required=False)
    project_skill = forms.MultipleChoiceField(label="Skill", choices=skill_choice,
                                          widget=forms.CheckboxSelectMultiple,required=False)

    class Meta:
        model = Project
        fields = ['name','description','project_platform','project_skill']


    # created_at = forms.DateTimeField('date created')
    # updated_at = forms.DateTimeField('date updated')

