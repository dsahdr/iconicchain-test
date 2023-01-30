from django.db.models import QuerySet
from django.http import HttpRequest
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.organizations.models import StoredFileHistory
from src.organizations.serializers import FileHistorySerializer
from src.users.exceptions import UserNotFound
from src.users.models import OrganizationUser


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]

    @swagger_auto_schema(
        operation_description="Login",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "token": openapi.Schema(type=openapi.TYPE_STRING),
                    "expiry": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        },
    )
    def post(self, request, format=None):  # noqa A002
        return super().post(request, format)  # noqa A002


class UserDownloadsView(ListAPIView):
    serializer_class = FileHistorySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("username", openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self: "ListAPIView", request: "HttpRequest", *args, **kwargs) -> "Response":
        return super().get(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet:
        username = self.request.query_params.get("username", "")
        user = OrganizationUser.objects.filter(username__icontains=username).first()
        if not user:
            raise UserNotFound
        return StoredFileHistory.objects.user(user)
