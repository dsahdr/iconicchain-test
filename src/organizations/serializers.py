from rest_framework.serializers import FileField, ModelSerializer

from src.organizations.models import StoredFile


class FileUploadSerializer(ModelSerializer):
    file = FileField()

    class Meta:
        model = StoredFile
        fields = ("file",)

    def create(self, validated_data: dict) -> "StoredFile":
        return self.Meta.model.objects.create(
            **validated_data, uploader=self.context["uploader"]
        )
