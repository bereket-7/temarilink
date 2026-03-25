from rest_framework import serializers
from apps.notifications.models import SMSMessage

class SMSMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSMessage
        fields = '__all__'
