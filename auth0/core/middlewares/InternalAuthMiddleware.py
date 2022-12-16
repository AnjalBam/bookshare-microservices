from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.conf import settings

client = settings.REDIS_CLIENT

class InternalAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def unauthorized_response(self, request):
        response = Response(
            {"detail": "Unauthorized request."},
            content_type="application/json",
            status=status.HTTP_401_UNAUTHORIZED,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        return response


    def __call__(self, request):
        auth_header = request.headers.get('x-request-auth-header', None)
        if not auth_header:
            return self.unauthorized_response(request)
        print(auth_header)
        is_authorized = client.get(auth_header)
        if not is_authorized:
            return self.unauthorized_response(request)

        return self.get_response(request)
