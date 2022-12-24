from rest_framework import serializers
from categories.models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',   
            'title',
            'slug',
            'published',
            )