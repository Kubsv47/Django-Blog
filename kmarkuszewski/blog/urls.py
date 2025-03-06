from django.urls import path
from .views import post_list
from .views import PostListAPIView

urlpatterns = [
    path('', post_list, name='home'),  
    path('posts/', post_list, name='post_list'),
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
 ]