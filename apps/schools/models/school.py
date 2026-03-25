from django.db import models
from apps.common.models import BaseModel

class School(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
