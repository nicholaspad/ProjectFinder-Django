import os

from .utils import send_email

OVERDUE_SUBJECT = "COS333 ProjectFinder entry past due"
OVERDUE_MESSAGE = """Hello,
Your project grade has been penalized because you did not create an entry in ProjectFinder before the due date. Please contact course staff if you believe this is incorrect.
- COS333 Staff"""

REMINDER_SUBJECT = "COS333 ProjectFinder entry reminder"
REMINDER_MESSAGE = """Hello,
Just a reminder that your ProjectFinder entry is due tomorrow (visit the website for the exact time). Please remember to fill out the project name and description fields!
- COS333 Staff"""


def send_overdue_email():
    header = f"Subject: {OVERDUE_SUBJECT}\n\n"
    message = header + OVERDUE_MESSAGE
    to = ["nicholaspad@princeton.edu", "nicholaspad@gmail.com"]

    send_email(
        to,
        message,
        os.getenv("EMAIL_PW", ""),
    )


def send_reminder_email():
    header = f"Subject: {REMINDER_SUBJECT}\n\n"
    message = header + REMINDER_MESSAGE
    to = ["nicholaspad@princeton.edu", "nicholaspad@gmail.com"]

    send_email(
        to,
        message,
        os.getenv("EMAIL_PW", ""),
    )
