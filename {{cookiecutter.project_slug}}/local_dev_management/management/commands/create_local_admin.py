from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = "Creates LOCAL_ADMIN_USERNAME superuser if does not exist"

    def handle(self, *args, **options):
        try:
            User.objects.get(username=settings.LOCAL_ADMIN)
            print("local admin user already exists")
        except User.DoesNotExist:
            print("creating local admin user, see settings for credentials")
            u = User.objects.create_user(
                settings.LOCAL_ADMIN,
                "",
                settings.LOCAL_PASS,
                is_staff=True,
                is_superuser=True,
            )
