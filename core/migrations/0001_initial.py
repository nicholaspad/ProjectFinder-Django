# Generated by Django 4.1 on 2022-08-22 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Config",
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
                    "due_date",
                    models.DateTimeField(help_text="Due date for ProjectFinder entry"),
                ),
            ],
        ),
    ]
