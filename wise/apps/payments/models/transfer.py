from django.conf import settings
from django.db import models

from .currency import Currency


class Transfer(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_transfers",
    )

    recipient_name = models.CharField(max_length=255)
    recipient_account = models.CharField(max_length=255)
    recipient_bank = models.CharField(max_length=255)
    recipient_country = models.CharField(max_length=2)

    source_currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="outgoing_transfers",
    )
    target_currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="incoming_transfers",
    )

    source_amount = models.DecimalField(max_digits=18, decimal_places=2)
    target_amount = models.DecimalField(max_digits=18, decimal_places=2)
    fx_rate = models.DecimalField(max_digits=18, decimal_places=8)

    STATUS = (
        ("created", "Created"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("cancelled", "Cancelled"),
    )
    status = models.CharField(max_length=20, choices=STATUS, default="created")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transfer {self.id} - {self.status}"
