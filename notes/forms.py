from dataclasses import fields
from pyexpat import model
from turtle import title
from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'note')

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('En validation kan smides, hvis der ikke står Django i titlen')
        return title
