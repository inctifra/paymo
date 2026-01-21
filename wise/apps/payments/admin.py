from django.contrib import admin

from .models import Balance
from .models import Currency
from .models import FeeRule
from .models import FXRate
from .models import Transaction
from .models import TransactionLimit
from .models import Transfer
from .models import Wallet


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active")
    search_fields = ("code", "name")


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("user", "is_active", "created_at")


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("wallet", "currency", "amount")


@admin.register(FXRate)
class FXRateAdmin(admin.ModelAdmin):
    list_display = ("base_currency", "quote_currency", "rate", "fetched_at")


@admin.register(FeeRule)
class FeeRuleAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage", "flat_fee", "currency", "is_active")


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "source_amount", "status", "created_at")
    list_filter = ("status",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_type", "amount", "currency", "wallet", "created_at")
    readonly_fields = ("created_at",)


@admin.register(TransactionLimit)
class TransactionLimitAdmin(admin.ModelAdmin):
    list_display = ("country", "daily_limit", "monthly_limit", "currency")
