from .models import Todo
from rest_framework import viewsets
from .serializers import Todoserializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer
