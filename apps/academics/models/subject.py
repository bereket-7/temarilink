from django.db import models
from apps.common.models import BaseModel
from apps.schools.models import School

class Subject(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
