from rest_framework.viewsets import ModelViewSet
from post.models import *
from post.api.serializer import *
class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)