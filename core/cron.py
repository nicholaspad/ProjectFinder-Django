import os

from django.contrib.auth.models import User
from django.db.models import Q

from .utils import send_email

OVERDUE_SUBJECT = "COS333 ProjectFinder entry past due"
OVERDUE_MESSAGE = """Hello,
Your project grade has been penalized because you did not create an entry in ProjectFinder before the due date. Please contact course staff if you believe this is incorrect.
- COS333 Staff"""

REMINDER_SUBJECT = "COS333 ProjectFinder entry reminder"
REMINDER_MESSAGE = """Hello,
Just a reminder that your ProjectFinder entry is due tomorrow (visit the website for the exact time). Please remember to fill out the project name and description fields!
- COS333 Staff"""

BATCH_SIZE = 50


def send_overdue_email():
    header = f"Subject: {OVERDUE_SUBJECT}\n\n"
    message = header + OVERDUE_MESSAGE
    to = []
    for user in User.objects.filter(~Q(username="admin"), entry__isnull=True):
        if user.username == "admin":
            continue
        if user.email:
            to.append(user.email)
            continue
        netid = user.username.split("-")[-1]
        to.append(f"{netid}@princeton.edu")

    for i in range(0, len(to), BATCH_SIZE):
        send_email(
            to[i : i + BATCH_SIZE],
            message,
            os.getenv("EMAIL_PW", ""),
        )


def send_reminder_email():
    header = f"Subject: {REMINDER_SUBJECT}\n\n"
    message = header + REMINDER_MESSAGE
    to = []
    for user in User.objects.filter(~Q(username="admin")):
        if user.username == "admin":
            continue
        if user.email:
            to.append(user.email)
            continue
        netid = user.username.split("-")[-1]
        to.append(f"{netid}@princeton.edu")

    for i in range(0, len(to), BATCH_SIZE):
        send_email(
            to[i : i + BATCH_SIZE],
            message,
            os.getenv("EMAIL_PW", ""),
        )
