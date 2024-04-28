from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
@api_view(['Post'])
def register(request):
  data = request.data

  user = RegisterSerializer(data=data)

  if user.is_valid():
    if User.objects.filter(username=data['email']).exists():
      return Response({'message': 'This user already exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
      user = User.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        username = data['email'],
        password = make_password(data['password'])
      )
      return Response({'message': 'User Register Success'}, status=status.HTTP_201_CREATED)
  else:
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMe(request):
  user = request.user

  serializer = UserSerializer(user, many=False)

  return Response(serializer.data)

