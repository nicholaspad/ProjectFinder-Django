# Generated by Django 4.1 on 2022-08-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="config",
            name="due_date",
            field=models.DateTimeField(
                help_text="Due date (Eastern Time) for ProjectFinder entry"
            ),
        ),
    ]
