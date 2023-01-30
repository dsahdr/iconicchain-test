from django.urls import path

from src.organizations.views import FileUploadView

urlpatterns = [
    path("file_upload/", FileUploadView.as_view()),
]
