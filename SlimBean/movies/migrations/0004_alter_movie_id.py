# Generated by Django 4.2.11 on 2024-03-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_remove_movie_created_at_remove_movie_identifier_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
