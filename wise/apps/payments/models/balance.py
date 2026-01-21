from decimal import Decimal

from django.db import models

from .currency import Currency
from .wallet import Wallet


class Balance(models.Model):
    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="balances",
    )
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    amount = models.DecimalField(
        max_digits=18, decimal_places=2, default=Decimal("0.00"),
    )

    class Meta:
        unique_together = ("wallet", "currency")

    def __str__(self):
        return f"{self.wallet.user.email} - {self.currency.code}: {self.amount}"
