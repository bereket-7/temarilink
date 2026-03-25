from django.db import models
from apps.common.models import BaseModel
from apps.students.models import Student
from apps.academics.models import Term

class ReportCard(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    pdf_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Report Card: {self.student.full_name} ({self.term.name})"
