from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from django.conf import settings

client = settings.REDIS_INSTANCE


class RequestAuthMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def unauthorized_response(self, request, message=""):
        if not message:
            message = "This headers are missing, so you're Not authorized"
        response = Response(
            {"message": message},
            content_type="application/json",
            status=status.HTTP_403_FORBIDDEN,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()

        return response

    def __call__(self, request, *args, **kwds):
        # code before execution of view
        key = request.headers.get("x-request-auth-header")
        if not key:
            print("No request auth header")
            return self.unauthorized_response(request)

        value = client.get(key)
        if not value:
            return self.unauthorized_response(
                request, message="Invalid request headers"
            )
            
        client.expire(key, 0);
        return self.get_response(request)
