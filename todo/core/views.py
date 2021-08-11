from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskSerializer
from .models import Task
from .permissions import IsOwner


class TestViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permissions = [IsAuthenticated, IsOwner]
