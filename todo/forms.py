from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'priority', 'status', 'category']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'due_date': 'Date',
            'priority': 'Priority',
            'status': 'Status',
            'category': 'Category',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
