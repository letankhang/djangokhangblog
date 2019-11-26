from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchResultsView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    #after url post/... must be string so we put last


]