from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getMe(request):
  user = request.user

  serializer = UserSerializer(user, many=False)

  return Response(serializer.data)

