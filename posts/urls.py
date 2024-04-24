from django.urls import path, include
from .views import helloWorld, PostViewSet, getAllPosts, createPost, getPostById, deletePost, updatePost
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('hello/', helloWorld, name='hello'),
    path('', getAllPosts, name='getAllPosts'),
    path('create/', createPost, name='createPost'),
    path('<str:pk>/', getPostById, name='getPost'),
    path('<str:pk>/delete/', deletePost, name='deletePost'),
    path('<str:pk>/update/', updatePost, name='updatePost'),
    path('', include(router.urls))
]
