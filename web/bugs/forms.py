from django import forms
from .models import Bug

class BugForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)

    def save(self, commit=True):
        bug = Bug(name=self.cleaned_data['name'])
        if commit:
            bug.save()
