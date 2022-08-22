# Generated by Django 4.1 on 2022-08-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_config_due_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("created_date", models.DateTimeField(auto_now=True)),
                (
                    "skills",
                    models.TextField(
                        default="",
                        help_text="Comma-separated list of frameworks and technologies",
                    ),
                ),
                (
                    "interests",
                    models.TextField(
                        default="",
                        help_text="Statement of general project interests",
                        max_length=150,
                    ),
                ),
                ("project_name", models.CharField(default="", max_length=50)),
                ("project_description", models.TextField(default="", max_length=150)),
            ],
        ),
    ]