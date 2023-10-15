from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book

# Create your views here.
@api_view(["GET"])
def books(request):
    books = Book.objects.values("title")
    return JsonResponse(
        data={"data": list(books)},
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
