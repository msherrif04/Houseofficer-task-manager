from rest_framework.serializers import ModelSerializer
from .models import Bed,Task


class BedSerializer(ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
