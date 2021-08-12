from django.urls.conf import path
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter

from .views import DaysetCreateAPIView, TaskViewSet


urlpatterns = [
    path('', DaysetCreateAPIView.as_view())
]

router = SimpleRouter()
router.register('tasks', TaskViewSet)
urlpatterns += router.urls
