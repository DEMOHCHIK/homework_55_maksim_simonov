import datetime
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'full_description', 'status', 'due_date']

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < datetime.date.today():
            raise forms.ValidationError('Дедлайн не может быть в прошлом.')
        return due_date