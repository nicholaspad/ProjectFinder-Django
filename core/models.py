from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Config(models.Model):
    due_date = models.DateTimeField(
        help_text="Due date (Eastern Time) for ProjectFinder entry"
    )


class ConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Config.objects.all().count()
        if count == 0:
            return True

        return False


class Entry(models.Model):
    author = models.OneToOneField(
        User, default=None, on_delete=models.CASCADE, related_name="entry"
    )
    created_date = models.DateTimeField(auto_now=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    skills = models.TextField(
        default="",
        help_text="Comma-separated list of frameworks and technologies",
    )
    interests = models.TextField(
        default="", help_text="Statement of general project interests"
    )
    project_name = models.CharField(max_length=100, default="")
    project_description = models.TextField(default="")


class EmailLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    email = models.CharField(max_length=100)
    date = models.DateTimeField()
