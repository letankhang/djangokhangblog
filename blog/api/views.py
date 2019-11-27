from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView,
)
from blog.models import Post
from .serializers import PostListSerializers, PostDetailSerializers, PostCreateUpdateSerializers
from django.utils.text import slugify

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostListSerializers
    # def get_queryset(self):

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostDetailSerializers
    lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostCreateUpdateSerializers
    lookup_field = 'slug'

class PostDeteleAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostDetailSerializers
    lookup_field = 'slug'

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostCreateUpdateSerializers
    # lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
