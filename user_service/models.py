import uuid
from django.db import models

# Create your models here.

class UserModels(models.Model):
    user_type_choices = [
        ("regular", "regular"),
        ("VIP", "VIP"),
        ("wholesale", "wholesale")
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    user_type = models.CharField(max_length=9, choices=user_type_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
