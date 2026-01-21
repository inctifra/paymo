from django.db import models

from .currency import Currency


class TransactionLimit(models.Model):
    country = models.CharField(max_length=2)
    daily_limit = models.DecimalField(max_digits=18, decimal_places=2)
    monthly_limit = models.DecimalField(max_digits=18, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    def __str__(self):
        return f"Limits for {self.country}"
