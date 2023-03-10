"""
iconicchain URL Configuration
"""
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from src.settings import config

schema_view = get_schema_view(
    openapi.Info(
        title=config.SWAGGER_TITLE,
        default_version="v1",
        description=config.SWAGGER_DESCRIPTION,
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "api/v1/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/v1/users/", include("src.users.urls")),
    path("api/v1/organizations/", include("src.organizations.urls")),
]
