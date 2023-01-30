from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.organizations.exceptions import FileNotFound, OrganizationNotFound
from src.organizations.models import Organization, StoredFile, StoredFileHistory
from src.organizations.serializers import FileSerializer, FileUploadSerializer
from src.responses import error_response
from src.settings import MEDIA_ROOT


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


class OrganizationFilesView(ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="View all files uploaded by organization members",
        manual_parameters=[
            openapi.Parameter(
                "organization_name", openapi.IN_QUERY, type=openapi.TYPE_STRING
            ),
        ],
    )
    def get(self: "ListAPIView", request: "HttpRequest", *args, **kwargs) -> "Response":
        return super().get(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet:
        organization_name = self.request.query_params.get("organization_name", "")
        organization = Organization.objects.filter(
            name__iexact=organization_name
        ).first()
        if not organization:
            raise OrganizationNotFound
        return StoredFile.objects.organization(organization)


class DownloadFilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self: "APIView", request: "HttpRequest", filename: str) -> "HttpResponse":
        file = StoredFile.objects.filter(file=filename).first()
        if not file:
            raise FileNotFound
        # create download history
        StoredFileHistory.objects.create(file=file, downloader=request.user)
        # return "static" serve function's response as a native view from MEDIA_URL
        return serve(request, filename, document_root=MEDIA_ROOT)
