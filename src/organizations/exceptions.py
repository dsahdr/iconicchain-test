from rest_framework.exceptions import APIException


class OrganizationNotFound(APIException):
    status_code = 404
    default_detail = "Organization not found"


class FileNotFound(APIException):
    status_code = 404
    default_detail = "File not found"
