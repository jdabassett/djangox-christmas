from django.db import models
from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.conf import settings


class NoteForSanta(models.Model):
    name = models.CharField(verbose_name="What is your name?", max_length=30)
    is_nice = models.BooleanField(verbose_name="Have you been good this year?", default=False)
    wishlist = models.TextField(verbose_name="What would you like for Christmas?", max_length=250)
    date = models.DateField(auto_now=True)
    # created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("note_detailed", kwargs={"pk": self.id})
