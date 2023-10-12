from rest_framework import authentication
from rest_framework import exceptions
from .models import User

class AccountAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.data.get("email", None)
        if not email:
            return None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such email')

        return (email, None)