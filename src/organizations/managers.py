from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from src.organizations.models import Organization
    from src.users.models import OrganizationUser


class StoredFileQuerySet(models.QuerySet):
    def user(self, user: "OrganizationUser") -> models.QuerySet:
        return self.filter(uploader=user)

    def organization(self, organization: "Organization") -> models.QuerySet:
        return self.filter(uploader__organization=organization)


class StoredFileManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return StoredFileQuerySet(self.model, using=self._db)

    def user(self, user: "OrganizationUser") -> models.QuerySet:
        """filter queryset by uploading user"""
        return self.get_queryset().user(user)

    def organization(self, organization: "Organization") -> models.QuerySet:
        """filter queryset by uploader's organization"""
        return self.get_queryset().organization(organization)


class StoredFileHistoryQuerySet(models.QuerySet):
    def user(self, user: "OrganizationUser") -> models.QuerySet:
        return self.filter(downloader=user)

    def organization(self, organization: "Organization") -> models.QuerySet:
        return self.filter(file__downloader__organization=organization)


class StoredFileHistoryManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return StoredFileHistoryQuerySet(self.model, using=self._db)

    def user(self, user: "OrganizationUser") -> models.QuerySet:
        """filter queryset by downloading user"""
        return self.get_queryset().user(user)

    def organization(self, organization: "Organization") -> models.QuerySet:
        """filter queryset by downloader's organization"""
        return self.get_queryset().organization(organization)
