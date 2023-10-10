from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from .models import User

def createAuthToken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(createAuthToken, sender=User)