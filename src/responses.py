from drf_yasg import openapi

error_response = openapi.Response(
    description="Return json with error from serializer",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "error": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
)
