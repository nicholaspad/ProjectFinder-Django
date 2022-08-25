import pytz
from datetime import datetime

from .models import Config


def get_username_from_netid(netid):
    return f"cas-princeton-{netid}"


def is_past_due():
    config = Config.objects.first()
    return config.due_date < datetime.now(tz=pytz.timezone("US/Eastern"))
