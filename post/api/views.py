from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from post.models import *
from post.api.serializer import *
from post.api.permission import *

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = ('slug')
    permission__classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_filds = ['catgory','category__slug']
    #filterset_filds = ['category']
    