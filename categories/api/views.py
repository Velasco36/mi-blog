from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import *
from categories.api.permissions  import *



class CategoryApiViewset(ModelViewSet):
    permission_classes= [IsAdminOrReadOnlyPermission]
    serializer_class = CategorySerializers
    queryset= Category.objects.all()
    #queryset = Category.objects.filter(published=True)
    name='Category-list'
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']