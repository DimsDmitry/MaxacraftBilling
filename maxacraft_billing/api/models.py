import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('minecraft-server', 'Minecraft Server'),
        ('web', 'Web'),
    ]

    ACCOUNT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('blocked', 'Blocked'),
        ('closed', 'Closed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(choices=ACCOUNT_TYPE_CHOICES, max_length=20)
    serverId = models.CharField(max_length=100, null=True, blank=True)
    userId = models.CharField(max_length=100)
    status = models.CharField(choices=ACCOUNT_STATUS_CHOICES, max_length=20)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    TRADE_TYPE_CHOICES = [
        ('auction', 'Auction'),
        ('gift', 'Gift'),
        ('trade', 'Trade'),
        ('credit', 'Credit'),
        ('stock_market', 'Stock Market'),
    ]

    TRANSACTION_TYPE_CHOICES = [
        ('inbound_transfer', 'Inbound Transfer'),
        ('outbound_transfer', 'Outbound Transfer'),
        ('freezing', 'Freezing'),
        ('refill', 'Refill'),
        ('inbound_payment', 'Inbound Payment'),
        ('outbound_payment', 'Outbound Payment'),
        ('reward', 'Reward'),
        ('credit_payment', 'Credit Payment'),
        ('credit_percentage', 'Credit Percentage'),
        ('dividends', 'Dividends'),
        ('salary_inbound', 'Salary Inbound'),
        ('salary_outbound', 'Salary Outbound'),
    ]

    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
        ('declined', 'Declined'),
        ('refunded', 'Refunded'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    accountId = models.ForeignKey('UserAccount', on_delete=models.CASCADE)
    trade_type = models.CharField(choices=TRADE_TYPE_CHOICES, max_length=20)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE_CHOICES, max_length=20)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)

    def __str__(self):
        return str(self.id)





