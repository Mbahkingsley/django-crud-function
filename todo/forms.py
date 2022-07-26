from django import forms
from .models import TodoModel

class TodoAppForm(forms):
    class Meta:
        model = TodoModel
        fields = [
            'title',
            'description',
            'time'
        ]
        
