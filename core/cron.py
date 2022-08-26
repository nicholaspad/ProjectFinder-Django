import os
import pytz
from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Q

from .models import Config
from .utils import log_email, send_email

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
    due_date = Config.objects.first().due_date
    diff = datetime.now(tz=pytz.timezone("US/Eastern")) - due_date
    # scheduler should run once a day
    if diff.days != 1:
        return

    header = f"Subject: {OVERDUE_SUBJECT}\n\n"
    message = header + OVERDUE_MESSAGE
    to = []

    users = User.objects.filter(~Q(username="admin"), entry__isnull=True)
    for user in users:
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

    log_email(users, "overdue")


def send_reminder_email():
    due_date = Config.objects.first().due_date
    diff = due_date - datetime.now(tz=pytz.timezone("US/Eastern"))
    # scheduler should run once a day
    if diff.days != 1:
        return

    header = f"Subject: {REMINDER_SUBJECT}\n\n"
    message = header + REMINDER_MESSAGE
    to = []

    users = User.objects.filter(~Q(username="admin"))
    for user in users:
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

    log_email(users, "reminder")
