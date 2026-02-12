from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    
   
    # photo_book = serializers.ImageField(required=False, allow_null=True)
    # photo_author = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Book
        fields = "__all__"
