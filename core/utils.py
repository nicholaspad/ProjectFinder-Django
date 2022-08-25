import pytz
from datetime import datetime, timedelta

from .models import Config


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
