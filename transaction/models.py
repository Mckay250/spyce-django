import uuid
from jsonfield import JSONField
from django.db import models


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length = 150)
    items = JSONField()
    prices = JSONField()
    types = JSONField()
    links = models.TextField()
    total = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)