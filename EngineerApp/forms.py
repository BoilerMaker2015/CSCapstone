from django.forms import ModelForm
from .models import Engineer

class EngineerForm(ModelForm):
    class Meta:
        model = Engineer
        fields = '__all__'
