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





