from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
import uuid


def image_upload_path(instance, filename):

    return "user_{0}/dp/{1}".format(instance.id, uuid.uuid4())


class MyUser(AbstractUser):
    id = models.UUIDField(
        verbose_name="User Id", default=uuid.uuid4, primary_key=True, unique=True
    )
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_verified = models.BooleanField(verbose_name="Is Verified", default=False)
    is_google_linked = models.BooleanField(verbose_name="Google Link", default=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="users",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="users",
        related_query_name="user",
    )


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
