from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'note']
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
