from rest_framework import serializers

from .models import Book, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre']
