from rest_framework import viewsets
from apps.notifications.models import SMSMessage
from .serializers import SMSMessageSerializer

class SMSMessageViewSet(viewsets.ModelViewSet):
    queryset = SMSMessage.objects.all()
    serializer_class = SMSMessageSerializer
    filterset_fields = ['school', 'status']
    search_fields = ['phone', 'message']
    ordering_fields = ['created_at']
