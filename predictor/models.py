from django.db import models

class PredictionHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    account_type = models.CharField(max_length=80)
    device_used = models.CharField(max_length=80)
    merchant_type = models.CharField(max_length=80)
    loyalty_program = models.CharField(max_length=8)
    time_of_day = models.CharField(max_length=40)
    transaction_date = models.DateField()
    predicted_category = models.CharField(max_length=100)

    class Meta:
        ordering = ["-created_at"]
