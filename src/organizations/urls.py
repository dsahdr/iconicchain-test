from django.urls import path

from src.organizations.views import (
    DownloadFilesView,
    FileUploadView,
    OrganizationFilesView,
    OrganizationsView,
)

urlpatterns = [
    path("file_upload/", FileUploadView.as_view()),
    path("files/", OrganizationFilesView.as_view()),
    path("", OrganizationsView.as_view()),
    path("download/<str:filename>/", DownloadFilesView.as_view()),
]
