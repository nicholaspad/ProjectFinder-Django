import pytz
import smtplib
import ssl
from datetime import datetime, timedelta

from .models import Config, EmailLog


def send_email(to_email, message, sender_pw):
    port = 587
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "tigersnatch@princeton.edu"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, sender_pw)
        server.sendmail(sender_email, to_email, message.strip())


def log_email(users, email_type):
    for user in users:
        EmailLog(
            user=user,
            date=datetime.now(tz=pytz.timezone("US/Eastern")),
            email_type=email_type,
        ).save()


def get_username_from_netid(netid):
    return f"cas-princeton-{netid}"


def is_past_due():
    config = Config.objects.first()
    return config.due_date < datetime.now(tz=pytz.timezone("US/Eastern"))


def _dt_to_cron_str(dt):
    return f"{dt.minute} {dt.hour} {dt.day} {dt.month} {dt.strftime('%a')}"


def get_overdue_email_cron_str():
    config = Config.objects.first()
    return _dt_to_cron_str(config.due_date + timedelta(minutes=1))


def get_reminder_email_cron_str():
    config = Config.objects.first()
    return _dt_to_cron_str(config.due_date - timedelta(days=1))
