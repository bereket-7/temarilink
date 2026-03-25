from django.db import models
from apps.common.models import BaseModel
from apps.students.models import Student

class Fee(BaseModel):
    PAID = 'PAID'
    UNPAID = 'UNPAID'
    STATUS_CHOICES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=UNPAID)
    due_date = models.DateField()

    def __str__(self):
        return f"Fee: {self.student.full_name} - {self.amount} ({self.status})"
