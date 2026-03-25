from django.db import models
from apps.common.models import BaseModel
from .student import Student

class Guardian(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='guardians')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Guardian of {self.student.full_name}"
