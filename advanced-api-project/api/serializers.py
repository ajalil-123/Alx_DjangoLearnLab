
from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
      model = Book
      fields =  ['title','publication_year','author']

     #Custom field-level validation for publication_year

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'book' ]