from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import tasks

class taskform(forms.ModelForm):
    class Meta:
        model=tasks
        fields=['task']
        widgets = {
            'task':forms.TextInput(attrs={'class':'container form-control input-group-lg','placeholder':'Enter task here'})
        }



