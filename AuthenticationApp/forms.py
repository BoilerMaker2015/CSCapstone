"""AuthenticationApp Forms
Created by Naman Patwari on 10/4/2016.
"""
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import MyUser,Student,Engineer,Professor,Platform,Skill
from CompaniesApp.models import Company
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models



class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    """A form to creating new users. Includes all the required
    fields, plus a repeated password."""
    email = forms.CharField(label='Email', widget=forms.EmailInput, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=True)

    firstname = forms.CharField(label="First name", widget=forms.TextInput, required=False)
    lastname = forms.CharField(label="Last name", widget=forms.TextInput, required=False)
    #lastname = tinymce_models.HTMLField()
    # gives the option of either to register as a student,teacher or engineer
    PART_CHOICES = (
        ('Student', 'Student'),
        ('Professor', 'Professor'),
        ('Engineer', 'Engineer'),)
    choice = forms.ChoiceField(label="Choice",choices=PART_CHOICES)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Check if email exists before
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This email has already been taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("There was an error, please contact us later")


class UpdateForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name', 'last_name')

    def clean_password(self):
        return self.initial["password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Check is email has changed
        if email == self.initial["email"]:
            return email
        # Check if email exists before
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This email has already been taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("There was an error, please contact us later")

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        # Check is email has changed
        if first_name is None or first_name == "" or first_name == '':
            email = self.cleaned_data.get("email")
            return email[:email.find("@")]
        return first_name


"""Update Student Form"""
class UpdateStudentForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    year_choice = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    )

    platform_choice = []
    counter = 0

    for i in Platform.objects.all():
        choice = (i.platform, i.platform)
        platform_choice.insert(counter, choice)
        counter = counter + 1


    platform = forms.MultipleChoiceField(label="Platform",choices=platform_choice,widget=forms.CheckboxSelectMultiple)

    #year = forms.CharField(widget=TinyMCE)

    year = forms.ChoiceField(label="Year",choices=year_choice,required=False)
    #skills = forms.CharField(max_length=100,required=False)

    #testing = forms.CharField(max_length=100,widget=forms.Textarea)
    #testing = forms.CharField(widget=TinyMCE(attrs={'cols': 3, 'rows': 3}))
    #testing = forms.CharField(max_length=100,required=False)

    # favorite_colors = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=year_choice,
    # )
    #platform = forms.ChoiceField(label="Platform",choices=platform_choice,required=False)
    # platform = forms.MultipleChoiceField(label="Platform",choices=platform_choice,
    #                                        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = ('major','year', 'platform', 'skill')



"""Update Professor Form"""
class UpdateProfessorForm(forms.ModelForm):


    class Meta:
        model = Professor
        fields = ('university', 'phone', 'teachClass')


"""Update Engineer Form"""
class UpdateEngineerForm(forms.ModelForm):
    # PART_CHOICES = (
    #     ('Student', 'Student'),
    #     ('Professor', 'Professor'),
    #     ('Engineer', 'Engineer'),)
    #company = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    #company = forms.CharField(max_length=100)
    company = forms.CharField(widget=TinyMCE)


    #choice = forms.ChoiceField(label="Choice", choices=Company.objects.all())
    #something = forms.CharField(max_length=100)

    class Meta:
        model = Engineer
        fields = ('company', 'position', 'phone')










"""Admin Forms"""


class AdminUserCreationForm(forms.ModelForm):
    """A form for Admin to creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AdminUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for Admin for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()



    class Meta:
        model = MyUser
        # fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin')
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin','is_student','is_engineer','is_professor')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]