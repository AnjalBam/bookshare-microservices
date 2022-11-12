from rest_framework.response import Response


class RequestAuthMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        # code before execution of view
        print(request.headers)
        return Response({"message": "response from the middleware"}, status=400)
        response = self.get_response(request)
        return response
