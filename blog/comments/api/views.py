from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from comments.models import Comment
from comments.api.serializers import CommentSerializer


class CommentApiViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter]
    ordering = ['-created_at']