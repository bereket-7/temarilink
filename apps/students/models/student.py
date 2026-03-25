from django.db import models
from apps.common.models import BaseModel
from apps.schools.models import School

class Student(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)
    section = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
