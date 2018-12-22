from django import forms
from webapp.models import Food


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'photo', 'price']
