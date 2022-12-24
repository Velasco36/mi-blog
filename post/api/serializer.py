from rest_framework import serializers
from post.models import *

class PostSerializer(serializers.ModelSerializer):
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
    