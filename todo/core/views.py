from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import DaysetSerializer, TaskSerializer
from .models import Dayset, Task
from .permissions import IsOwner


class TaskViewSet(ModelViewSet):
    """
    A view set for viewing and editing task instances.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_contexst(self):
        context = self.super().get_serializer_context()
        context.update.update({'request': self.request})
        return context
    
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class DaysetCreateAPIView(generics.CreateAPIView):
    """
    View for creating daysets
    """
    queryset = Dayset.objects.all()
    serializer_class = DaysetSerializer
    permissions = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        This method creates new dayset and should be executed ones per day, if dayset was created today the response will be 400 status .
        """
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response("today's dayset already exiists", status=status.HTTP_400_BAD_REQUEST)
