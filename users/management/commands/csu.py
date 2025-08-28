import os

from django.core.management import BaseCommand
from users.models import User

Super_User_email = os.getenv("Super_User_email")
Super_User_password = os.getenv("Super_User_password")


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email=Super_User_email)
        user.set_password(Super_User_password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()