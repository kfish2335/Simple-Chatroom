from chat.models import chat
from rest_framework import viewsets, permissions
from .serializers import chatSerializer

class chatViewSet(viewsets.ModelViewSet):
    queryset = chat.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = chatSerializer