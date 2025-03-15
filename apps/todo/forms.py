from django import forms
from .models import *

class FormTodo(forms.ModelForm):
    deadline = forms.DateField(
        widget = forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats = ["%Y-%m-%d"],
        required = False,
    )
    class Meta:
        model = Todo
        fields = ('deadline', 'text')