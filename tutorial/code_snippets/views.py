from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

""" below class creates an api with all possible HTTP methods 
i.e. GET, POST, PUT and Delete for snippets model by importing the 
generics.RetrieveUpdateDestroyAPIView from django's rest_framework"""
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
