from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
  # return HttpResponse('Hello World')
  return render(request, 'posts/index.html')
