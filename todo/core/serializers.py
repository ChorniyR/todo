from rest_framework import serializers

from .models import Dayset, Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['title', 'state', 'owner', 'details'] 

    def create(self, validated_data):
        validated_data['dayset'] = Dayset.get_by_user(self.context['request'].user)
        return super().create(validated_data)


class DaysetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dayset
        fields = '__all__'

