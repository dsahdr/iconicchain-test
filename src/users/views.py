from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication


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
