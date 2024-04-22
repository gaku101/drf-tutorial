from django.urls import path, include
from .views import helloWorld, PostViewSet, getAllPosts
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('hello/', helloWorld, name='hello'),
    path('', getAllPosts, name='getAllPosts'),
    path('', include(router.urls))
]
