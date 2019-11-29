from rest_framework import serializers

from blog.models import Post


def post_crud_url(crud):
    return serializers.HyperlinkedIdentityField(
        view_name=f'api-post-{crud}',
        lookup_field='slug'
    )

class PostListSerializers(serializers.ModelSerializer):
    detail_url = post_crud_url('detail')
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            'author',
            # 'slug',
            # 'date_posted',
            'detail_url'
        ]

    def get_author(self, obj):
        return str(obj.author.username)

class PostDetailSerializers(serializers.ModelSerializer):
    delete_url = post_crud_url('delete')
    update_url = post_crud_url('update')
    author = serializers.SerializerMethodField()
    date_posted = serializers.SerializerMethodField()
    image_user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'image_user',
            'content',
            'slug',
            'date_posted',
            'update_url',
            'delete_url',
        ]

    def get_author(self, obj):
        return str(obj.author.username)

    def get_date_posted(self, obj):
        return  obj.date_posted.strftime('%m/%d/%Y %H:%M:%S')

    def get_image_user(self, obj):
        return obj.author.profile.image.url


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

