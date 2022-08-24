from django.contrib import admin
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
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    skills = models.TextField(
        default="",
        help_text="Comma-separated list of frameworks and technologies",
    )
    interests = models.TextField(
        default="", max_length=150, help_text="Statement of general project interests"
    )
    project_name = models.CharField(max_length=50, default="")
    project_description = models.TextField(default="", max_length=150)
