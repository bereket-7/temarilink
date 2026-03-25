from django.db import models
from apps.common.models import BaseModel
from apps.students.models import Student
from .subject import Subject
from .term import Term

class Grade(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='academic_grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name}: {self.score}"
