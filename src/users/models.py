from django.contrib.auth.models import AbstractUser
from django.db import models


class OrganizationUser(AbstractUser):
    """
    User model linked to the organisation
    """

    organization = models.ForeignKey(
        "organizations.Organization", related_name="users", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.username
