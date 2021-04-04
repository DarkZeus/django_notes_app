from django import forms
from .models import Task
from django.utils import timezone


class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(required=True, min_length=2, max_length=255)
    run_at = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'value': timezone.now().strftime("%Y-%m-%dT%H:%M")}))

    class Meta:
        model = Task
        fields = ['title', 'run_at']


class UpdateTaskForm(forms.ModelForm):
    title = forms.CharField(required=True, min_length=2, max_length=255)
    run_at = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format="%Y-%m-%dT%H:%M"))

    class Meta:
        model = Task
        fields = ['title', 'run_at']