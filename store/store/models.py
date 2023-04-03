from django.db import models
from helpers.models import BaseModel
# Create your models here.


class TestModel(models.Model):
    test = models.BooleanField(default=True)


class Owner(BaseModel, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.username} ({self.email})'
