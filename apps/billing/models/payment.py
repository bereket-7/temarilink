from django.db import models
from apps.common.models import BaseModel
from .fee import Fee

class Payment(BaseModel):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for Fee {self.fee.id}"
