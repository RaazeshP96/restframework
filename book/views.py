from django.shortcuts import render
from .serailizers import BookSerailizer
from .models import Book
from rest_framework import viewsets


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerailizer

