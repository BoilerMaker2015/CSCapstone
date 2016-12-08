from django import forms
class TeacherForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=120)
    last_name = forms.CharField(label='last_name', max_length=120)

class TeachClassForm(forms.Form):  
	title = forms.CharField(
        max_length = 120
 
    )   

class EmailForm(forms.Form):  
	email = forms.CharField(
    	max_length = 120

	)  

class ClassForm(forms.Form):  
    title = forms.CharField(
        max_length = 120

    )  
