from django.test import TestCase
from django.contrib.auth import get_user_model
from pages.models import NoteForSanta
from django.urls import reverse
# from django.contrib.auth.models import User

class TestNotes(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="username",password="password",email="email")
        self.note = NoteForSanta.objects.create(name='name', is_nice=False, wishlist="wishlist", created_by=self.user)

    def test_greet_status_code_templates_contents(self):
        response = self.client.get(reverse('greet'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "_base.html")
        self.assertTemplateUsed(response, "pages/greet.html")
        self.assertContains(response, "Send a note to Santa")

    def test_notes_status_code_templates_contents(self):
        response = self.client.get(reverse('notes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "_base.html")
        self.assertTemplateUsed(response, "pages/notes.html")
        self.assertContains(response, "name")

    def test_create_status_code_templates_contents(self):
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "_base.html")
        self.assertTemplateUsed(response, "pages/note_create.html")
        self.assertContains(response, "What would you like for Christmas?")

    def test_detailed_status_code_templates_contents(self):
        response = self.client.get(reverse('note_detailed', kwargs={"pk": self.note.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "_base.html")
        self.assertTemplateUsed(response, "pages/note_detailed.html")
        self.assertContains(response, f"Note from {self.note.name} to Santa!")

    def test_update_status_code_templates_contents(self):
        response = self.client.get(reverse('note_update', kwargs={"pk": self.note.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "_base.html")
        self.assertTemplateUsed(response, "pages/note_update.html")
        self.assertContains(response, "Last chance to change your note to Santa")

    def test_delete_status_code_templates_contents(self):
        response = self.client.get(reverse('note_delete', kwargs={"pk": self.note.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "_base.html")
        self.assertTemplateUsed(response, "pages/note_delete.html")
        self.assertContains(response, "Are you sure you want to delete this note?")

    def test_note_create(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("note_create"),
            {'name': "create", "wishlist": "wishlist"},
            follow=True
        )

        self.assertRedirects(response, reverse('note_detailed', kwargs={"pk": "2"}))
        self.assertContains(response, "<h1>Note from create to Santa!</h1>")

    def test_note_update(self):
        response = self.client.post(
            reverse("note_update", kwargs={'pk':1}),
            {'is_nice': True, "wishlist": "wishlist_update"},
            follow=True
        )
        self.assertRedirects(response, reverse('note_detailed', kwargs={"pk": "1"}))
        self.assertContains(response, "<p>Has been nice this year!</p>")

    def test_note_delete(self):
        response = self.client.delete(
            reverse("note_delete", kwargs={'pk':1}),
            follow=True
        )
        self.assertRedirects(response, reverse('notes'))






