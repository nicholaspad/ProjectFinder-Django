# Generated by Django 4.1 on 2022-08-23 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_entry"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="last_modified_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
