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

@api_view(['POST'])
def createPost(request):
  data = request.data
  user = request.user

  post = Post.objects.create(
    title = data['title'],
    content = data['content'],
    author = user
  )

  serializer = PostSerializer(post, many=False)
  return Response(serializer.data)

@api_view(['GET'])
def getPostById(request, pk):
  post = Post.objects.get(id=pk)

  serializer = PostSerializer(post, many=False)
  return Response(serializer.data)

@api_view(['DELETE'])
def deletePost(request, pk):
  post = Post.objects.get(id=pk)
  post.delete()

  return Response({'message': 'delete success'})

@api_view(['PUT'])
def updatePost(request, pk):
  data = request.data
  post = Post.objects.get(id=pk)

  post.title = data['title']
  post.content = data['content']
  post.published = data['published']

  post.save()

  serializer = PostSerializer(post, many=False)
  return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
