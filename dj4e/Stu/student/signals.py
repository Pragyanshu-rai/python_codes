from django.contrib.auth.models import User
from .models import *
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# for creating an auth token right after a user is registered
@receiver(post_save, sender=User)
def user_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print("Token Generated!")

