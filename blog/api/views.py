from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView,
)
from blog.models import Post
from .permissions import IsOwnerOrReadonly
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny
)

from .serializers import (
    PostListSerializers,
    PostDetailSerializers,
    PostCreateUpdateSerializers
)


class PostListAPIView(ListAPIView):
    # queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostListSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'author__id', 'date_posted', 'slug', 'id']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(author__username__icontains=query)|
                Q(content__icontains=query)|
                Q(date_posted__icontains=query)|
                Q(slug__icontains=query)
            )
        return queryset_list.order_by('-date_posted')


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostDetailSerializers
    lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostCreateUpdateSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadonly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class PostDeteleAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostDetailSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadonly]


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostCreateUpdateSerializers
    permission_classes = [IsAuthenticated]
    # lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
