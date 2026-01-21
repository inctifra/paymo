from django.db import models

from .balance import Balance
from .currency import Currency
from .transfer import Transfer
from .wallet import Wallet


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, on_delete=models.PROTECT)
    transfer = models.ForeignKey(
        Transfer, on_delete=models.SET_NULL, null=True, blank=True,
    )

    amount = models.DecimalField(max_digits=18, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    TRANSACTION_TYPE = (
        ("debit", "Debit"),
        ("credit", "Credit"),
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    reference = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.transaction_type.upper()} {self.amount} {self.currency.code}"
