# Generated by Django 4.2.5 on 2023-12-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NoteForSanta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=30, verbose_name="What is your name?"),
                ),
                (
                    "is_nice",
                    models.BooleanField(
                        default=False, verbose_name="Have you been good this year?"
                    ),
                ),
                (
                    "wishlist",
                    models.TextField(
                        max_length=250,
                        verbose_name="What would you like for Christmas?",
                    ),
                ),
                ("date", models.DateField(auto_now=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]