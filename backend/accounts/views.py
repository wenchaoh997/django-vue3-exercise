from django.http import JsonResponse
from rest_framework import status
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import decode_jwt

from .models import User
from .serializers import UserSerializer
from .permissions import AdminOnly

# Create your views here.

@swagger_auto_schema(
    method='post', 
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'UserName': openapi.Schema(type=openapi.TYPE_STRING, description='Email as username', example="example@gmail.com"),
            'Password': openapi.Schema(type=openapi.TYPE_STRING, description='Password', example="1234"),
        }
    )
)
@api_view(["POST"])
def loginApi(request):
    """Token login"""
    email = request.data.get("UserName", None)
    password = request.data.get("Password", None)
    try:
        user = User.objects.get(email=email)
        is_valid = user.check_password(password)
        if is_valid:
            token = user.token
            response = JsonResponse(
                status=status.HTTP_200_OK,
                data={
                    "token": token,
                    "message": "Login successed"
                }
            )
            return response
    except User.DoesNotExist:
        pass
    return JsonResponse(
        status=status.HTTP_400_BAD_REQUEST,
        data={
            "status": "false", "message": "Invalid email or password"
        },
    )


@swagger_auto_schema(
    method='post', 
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email as username', example="example@gmail.com"),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password', example="1234"),
        }
    )
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


@api_view(["POST"])
def login_verification(request):
    jwt_val = request.data.get("jwt", None)
    if not jwt_val: 
        return JsonResponse(
            status=status.HTTP_200_OK,
            data={"message": "None"},
        )
    djwt = decode_jwt(jwt_val)
    data = djwt.get("data", None)
    if not data:
        return JsonResponse(
            status=status.HTTP_200_OK,
            data={"message": "None"},
        )
    email = data.get("name", None)

    user = User.objects.filter(email=email)
    if user:
        return JsonResponse(
            status=status.HTTP_200_OK,
            data={"message": "OK"},
        )
    return JsonResponse(
        status=status.HTTP_200_OK,
        data={"message": "None"},
    )