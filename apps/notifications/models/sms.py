from django.db import models
from apps.common.models import BaseModel
from apps.schools.models import School

class SMSMessage(BaseModel):
    SENT = 'SENT'
    FAILED = 'FAILED'
    STATUS_CHOICES = [
        (SENT, 'Sent'),
        (FAILED, 'Failed'),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=SENT)

    def __str__(self):
        return f"SMS to {self.phone} - {self.status}"
