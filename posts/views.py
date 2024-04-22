from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def helloWorld(request):
  # return HttpResponse('Hello World')
  return render(request, 'posts/index.html')

@api_view(['GET'])
def getAllPosts(request):
  posts = Post.objects.all()

  serializer = PostSerializer(posts, many=True)

  return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
