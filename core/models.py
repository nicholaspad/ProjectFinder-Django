from django.db import models


class Config(models.Model):
    # Limit to one row?
    due_date = models.DateTimeField(
        help_text="Due date (Eastern Time) for ProjectFinder entry"
    )
