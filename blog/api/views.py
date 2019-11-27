from rest_framework.generics import ListAPIView

from blog.models import Post
from .serializers import PostSerializers


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializers
    # def get_queryset(self):
