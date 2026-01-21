from django.db import models

from .currency import Currency


class FXRate(models.Model):
    base_currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="base_rates",
    )
    quote_currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="quote_rates",
    )
    rate = models.DecimalField(max_digits=18, decimal_places=8)
    fetched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("base_currency", "quote_currency")

    def __str__(self):
        return f"{self.base_currency}/{self.quote_currency} = {self.rate}"
