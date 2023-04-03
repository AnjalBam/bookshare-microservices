from django.db import models
from helpers.fields import AutoIdxField
from django.utils import timezone

# Create your models here.

class BaseModel(models.Model):
    idx = AutoIdxField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
