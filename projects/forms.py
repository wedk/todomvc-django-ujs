# forms.py
from django.forms import ModelForm

from .models import Project, Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name']

    def clean_name(self):
        return self.cleaned_data.get('name', '').strip()


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']

    def clean_title(self):
        return self.cleaned_data.get('title', '').strip()


class ToggleTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['completed']