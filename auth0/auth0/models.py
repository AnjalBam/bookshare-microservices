from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _

from helpers.models import BaseModel


class MyUser(BaseModel, AbstractUser):
    IDX_PREFIX = 'usr'
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_verified = models.BooleanField(verbose_name="Is Verified", default=False)
    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self) -> str:
        return self.email

    @classmethod
    def get_token(self, user):
        refresh_token = RefreshToken.for_user(user=user)

        data = {}

        data["refresh"] = str(refresh_token)
        data["access"] = str(refresh_token.access_token)

        return data
