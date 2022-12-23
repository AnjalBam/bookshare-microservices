from rest_framework.response import Response

class ResponseMixin:
    def send_response(self, data=[], error=[], message="", status=200):
        response = {}
        if data:
            response['data'] = data
        if error:
            response['error'] = error
        if message:
            response['detail'] = message

        return Response(response, status=status)