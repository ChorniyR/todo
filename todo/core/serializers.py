from django.db.models import fields
from rest_framework import serializers
from django.db import IntegrityError

from .models import Dayset, Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['title', 'state', 'owner', 'details'] 

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        validated_data['dayset'] = Dayset.get_by_user(self.context['request'].user)
        return super().create(validated_data)


class DaysetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dayset
        fields = '__all__'

