from rest_framework import serializers
from .models import Todo

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')