from rest_framework import serializers

from blog.models import Post

class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'date_posted',
            'slug',
        ]

class PostDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'content',
            'date_posted',
            'slug',
        ]

class PostCreateUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'author',
            'content',
            'date_posted',
            # 'slug',
        ]