from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework.response import Response
from django.core import serializers

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import BookSerializer
from .models import Book, Author

# Create your views here.
@api_view(["GET"])
def books(request):
    books = Book.objects.values("title")
    return JsonResponse(
        data={"data": list(books)},
        status=status.HTTP_200_OK,
    )

@swagger_auto_schema(
    method='post', 
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='', example="YOLO"),
            'author': openapi.Schema(type=openapi.TYPE_INTEGER, description='', example=1),
            'summary': openapi.Schema(type=openapi.TYPE_STRING, description='', example="You only look once."),
            'isbn': openapi.Schema(type=openapi.TYPE_STRING, description='', example="11456789125"),
            'genre': openapi.Schema(
                type=openapi.TYPE_ARRAY, 
                items=openapi.Items(type=openapi.TYPE_STRING),
                description='', 
                example=["1", "2"]
            ),
        }
    )
)
@api_view(["GET", "POST"])
def bookList(request):
    if (request.method == "GET"):
        books = Book.objects.values()
        return JsonResponse(
            data={
                "books": list(books),
            },
            status=status.HTTP_200_OK,
        )
    elif (request.method == "POST"):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        authorInstance = Author.objects.get(id=serializer.validated_data.get("author"))

        book = Book.objects.create(
            title = serializer.validated_data.get("title"),
            author = authorInstance,
            summary = serializer.validated_data.get("summary"),
            isbn = serializer.validated_data.get("isbn"),
        )
        book.genre.set(serializer.validated_data.get("genre"))

        return JsonResponse(
            data={"message": "OK"},
            status=status.HTTP_200_OK,
        )

@api_view(["GET", "DELETE"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except:
        return JsonResponse(
            status=status.HTTP_400_BAD_REQUEST
        )
    if (request.method == "GET"):
        serializer = BookSerializer(book)
        return Response(
            data=serializer.data,

        )
    elif (request.method == "DELETE"):
        book.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
