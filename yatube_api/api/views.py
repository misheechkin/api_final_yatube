from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from posts.models import Follow
from .serializers import FollowSerializer


User = get_user_model()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follow.objects.all()

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)