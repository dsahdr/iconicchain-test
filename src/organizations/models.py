from django.core.files.base import File
from django.db import models
from django.utils import timezone

from src.organizations.managers import StoredFileHistoryManager, StoredFileManager


def image_upload_path(instance: "File", filename: str) -> str:
    return f"{filename}-{timezone.now().timestamp()}"


class Organization(models.Model):
    """
    A model representing an organization to which users are connected
    """

    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class StoredFile(models.Model):
    """
    A model representing a file uploaded by user
    """

    uploader = models.ForeignKey(
        "users.OrganizationUser", related_name="files", on_delete=models.CASCADE
    )
    file = models.FileField(
        upload_to=image_upload_path,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    objects = StoredFileManager()

    @property
    def organization(self) -> str:
        return self.uploader.organization

    @property
    def filename(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.filename} by {self.downloader.username}"


class StoredFileHistory(models.Model):
    file = models.ForeignKey(
        "organizations.StoredFile",
        related_name="download_history",
        on_delete=models.CASCADE,
    )
    downloader = models.ForeignKey(
        "users.OrganizationUser",
        related_name="download_history",
        on_delete=models.CASCADE,
    )
    downloaded_at = models.DateTimeField(auto_now_add=True)

    objects = StoredFileHistoryManager()

    def __str__(self) -> str:
        return f"Download of {self.file.filename} by {self.downloader.username} at {self.downloaded_at}"
