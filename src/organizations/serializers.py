from rest_framework.serializers import CharField, FileField, ModelSerializer

from src.organizations.models import Organization, StoredFile, StoredFileHistory


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ("name", "total_download_count")


class FileUploadSerializer(ModelSerializer):
    file = FileField()

    class Meta:
        model = StoredFile
        fields = ("file",)

    def create(self, validated_data: dict) -> "StoredFile":
        return self.Meta.model.objects.create(
            **validated_data, uploader=self.context["uploader"]
        )


class FileSerializer(ModelSerializer):
    uploader = CharField(source="uploader.username")

    class Meta:
        model = StoredFile
        fields = (
            "file",
            "uploader",
            "upload_timestamp",
            "download_count",
        )


class FileHistorySerializer(ModelSerializer):
    downloader = CharField(source="downloader.username")
    file = CharField(source="file.filename")

    class Meta:
        model = StoredFileHistory
        fields = ("file", "downloader", "download_timestamp")
