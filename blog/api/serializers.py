from rest_framework import serializers

from blog.models import Post

class PostSerializers(serializers.ModelSerializer):
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