from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from pages.models import NoteForSanta


class GreetPageView(TemplateView):
    template_name = "pages/greet.html"


class NoteDetailedView(DetailView):
    template_name = "pages/note_detailed.html"
    context_object_name = "note"
    model = NoteForSanta


class NotesView(ListView):
    model = NoteForSanta
    template_name = 'pages/notes.html'
    context_object_name = 'notes'


class NoteCreateView(CreateView):
    model = NoteForSanta
    fields = ["name", 'is_nice', 'wishlist']
    template_name = "pages/note_create.html"
    context_object_name = 'note_create'


class NoteUpdateView(UpdateView):
    model = NoteForSanta
    template_name = 'pages/note_update.html'
    fields = ['is_nice', 'wishlist']
    context_object_name = 'note_update'


class NoteDeleteView(DeleteView):
    model = NoteForSanta
    template_name = 'pages/note_delete.html'
    success_url = reverse_lazy("notes")
    context_object_name = 'note_delete'
