from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import unidecode
import shortuuid

from .models import User
from .serializers import UserSerializer
from .permissions import AdminOnly

# Create your views here.
@api_view(["POST"])
def loginApi(request):
    """Token login"""
    email = request.data.get("email", None)
    password = request.data.get("password", None)

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        print(f"[SERVER] Login successfully from {user}\n")
        token = Token.objects.get(user=user)
        return Response({"auth_token": token.key}, status=status.HTTP_200_OK)

    return JsonResponse(
        status=status.HTTP_400_BAD_REQUEST,
        data={"status": "false", "message": "Invalid email or password"},
    )


@api_view(["POST"])
def registerApi(request):
    """Create new account and response token"""
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        print(f"User {user} is created\n")

    else:
        print(f"[SERVER]: Error registering user {serializer.errors}")
        return JsonResponse(
            status=status.HTTP_400_BAD_REQUEST, data={"errors": serializer.errors}
        )

    return JsonResponse(status=status.HTTP_200_OK, data={"message": "User is created"})


# Utils Functions
def emailGenerator(fullName):
    """Generate an email from a fullname"""
    fullName = unidecode.unidecode(fullName)  # Remove accent from text
    words = fullName.split(" ")

    name = ""
    if len(words) >= 3:
        name = "".join([word[0].lower() for word in words])
    else:
        name = words[len(words) - 1].lower()

    userId = shortuuid.ShortUUID(alphabet="01345678").random(length=5)

    email = f"{name}D{userId}@kaz.company.com"

    return email