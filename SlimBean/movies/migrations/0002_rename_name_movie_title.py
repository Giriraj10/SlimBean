# Generated by Django 4.2.11 on 2024-03-27 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="name",
            new_name="title",
        ),
    ]
