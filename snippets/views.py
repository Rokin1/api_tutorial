from django.shortcuts import render
from snippets.models import Snippet

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from snippets.serializers import SnippetSerializer
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permission import IsAuthentication


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer