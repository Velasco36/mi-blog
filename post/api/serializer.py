from rest_framework import serializers
from post.models import *
from users.api.serializer import UserSerializer
from categories.api.serializers import CategorySerializers

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializers()
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'slug',
            'miniture',
            'created_at',
            'published',
            'user',
            'category'
            )
    