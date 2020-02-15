from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class PostViewset(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class CommentViewset(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
