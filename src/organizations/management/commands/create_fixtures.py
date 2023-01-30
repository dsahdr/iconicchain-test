from django.core.management.base import BaseCommand
from django.db import transaction

from src.organizations.models import Organization
from src.settings import config
from src.users.models import OrganizationUser


class Command(BaseCommand):
    """
    Provide initial db fixtures from config with 'manage.py create_fixtures.py'
    """

    @transaction.atomic
    def handle(self, *args, **options) -> None:
        help = "Create initial fixtures for Organizations and users"  # noqa F841

        """Create Organization objects"""
        for organization in config.ORGANIZATIONS:
            Organization.objects.get_or_create(
                name=organization.name,
            )

        """Create User objects if organization is valid"""
        for user in config.USERS:
            organization = Organization.objects.filter(name=user.organization).first()
            if (
                organization
                and not OrganizationUser.objects.filter(username=user.username).exists()
            ):
                OrganizationUser.objects.create_user(
                    username=user.username,
                    password=user.password,
                    organization=organization,
                )
