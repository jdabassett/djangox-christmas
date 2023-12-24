from django.urls import path

from .views import GreetPageView, NotesView, NoteDetailedView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path("", GreetPageView.as_view(), name="greet"),
    path("notes/", NotesView.as_view(), name="notes"),
    path("note/create/", NoteCreateView.as_view(), name="note_create"),
    path("note/<int:pk>/detailed/", NoteDetailedView.as_view(), name="note_detailed"),
    path("note/<int:pk>/update/", NoteUpdateView.as_view(), name="note_update"),
    path("note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
]
