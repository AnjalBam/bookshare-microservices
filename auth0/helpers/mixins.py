from rest_framework.response import Response
from rest_framework import status

from helpers.response_codes import response_codes


class ResponseMixin(object):
    """
    Mixin to add custom response format for consistency across the software.
    """

    def infer_default_detail(self, status_code: int = None) -> str:
        if status_code < 300 and status_code >= 200:
            message = 'Request Successful'
        elif status_code < 400 and status_code >= 300:
            message = 'Redirected Successfully'
        elif status_code < 500 and status_code >= 400:
            message = 'Client Error'
        elif status_code < 600 and status_code >= 500:
            message = 'Server Error'
        else:
            message = 'Unknown'
        return message

    def get_status(self, status_code: int = None) -> bool:
        if status_code < 300 and status_code >= 200:
            return True
        else:
            return False

    def send_response(self, data={},
                        status=status.HTTP_200_OK,
                        code=response_codes["success"],
                        detail=None):
        success_status = self.get_status(status)
        
        response = {}
        response['code'] = code
        response['detail'] = detail or self.infer_default_detail(
            status_code=status)
        response['status'] = success_status
        response['data' if success_status else 'error'] = data
        return Response(response, status=status)
