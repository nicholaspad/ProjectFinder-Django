from django.core.management.base import BaseCommand, CommandError

from core.cron import send_overdue_email, send_reminder_email

# python manage.py sendemails
class Command(BaseCommand):
    help = "Maybe sends reminder/overdue emails (depending on the current datetime). Meant to be run once a day (e.g. from Heroku Scheduler)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--test",
            action="store_true",
            help="Use this flag to manually send a reminder and overdue email to the specified address.",
        )
        parser.add_argument(
            "email",
            nargs="?",
            type=str,
            help="Provide an email address to receive the test reminder and overdue emails.",
        )

    def handle(self, *args, **options):
        is_test = options["test"]
        test_email = options["email"]

        if is_test:
            if not test_email:
                raise CommandError(
                    "Provide an email address when using --test. Example: python manage.py --test nick@gmail.com"
                )
            send_reminder_email(test_email=test_email)
            self.stdout.write("Sent test reminder email!")
            send_overdue_email(test_email=test_email)
            self.stdout.write("Sent test overdue email!")
            return

        send_reminder_email()
        self.stdout.write(
            "Maybe sent reminder emails! Check the EmailLog table for more info."
        )
        send_overdue_email()
        self.stdout.write(
            "Maybe sent overdue emails! Check the EmailLog table for more info."
        )
