from django.http import HttpRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.organizations.serializers import FileUploadSerializer
from src.responses import error_response


class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.FileUploadParser,
    )

    @swagger_auto_schema(
        operation_description="File upload",
        request_body=FileUploadSerializer(),
        responses={201: "Uploaded", 400: error_response},
    )
    def post(self: "APIView", request: "HttpRequest") -> Response:
        file_obj = request.FILES["file"]
        serializer = FileUploadSerializer(
            data={"file": file_obj}, context={"uploader": request.user}
        )
        serializer.is_valid()
        if serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response("Uploaded", status=status.HTTP_201_CREATED)
