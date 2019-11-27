from django.urls import path
from . import views
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeteleAPIView,
    PostCreateAPIView,
)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='api-blog-home'),

    # path('about/', views.about, name='blog-about'),
    #
    # path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    #
    path('create/', PostCreateAPIView.as_view(), name='api-post-create'),
    path('<str:slug>/delete/', PostDeteleAPIView.as_view(), name='api-post-delete'),
    path('<str:slug>/update/', PostUpdateAPIView.as_view(), name='api-post-update'),
    path('<str:slug>/', PostDetailAPIView.as_view(), name='api-post-detail'),
    # #after url post/... must be string so we put last


]