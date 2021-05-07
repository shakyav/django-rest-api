from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions # new

from .serializers import SnippetSerializer, UserSerializer # new
from .permissions import IsOwnerOrReadOnly # new

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    """Django Rest Framework ships with a number of permission 
    classes we could use to restrict access to a given view. 
    Here we will use IsAuthenticatedOrReadOnly to ensure that 
    authenticated requests have read-write access and 
    unauthenticated requests only have read-only access. """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new

    """ associate the snippet created y user to self(logged in user)  """
    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)

""" below class creates an api with all possible HTTP methods 
i.e. GET, POST, PUT and Delete for snippets model by importing the 
generics.RetrieveUpdateDestroyAPIView from django's rest_framework"""
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,) # new


class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
