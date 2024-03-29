from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

def paisa_de_exception_handler(exc, context):
    if isinstance(exc, Exception):
        exc = APIException(detail=str(exc))
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response