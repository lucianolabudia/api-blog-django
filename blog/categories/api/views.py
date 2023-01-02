from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializer import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'