class BSAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_token = request.headers.get('Authorization')
        print(jwt_token)
        response = self.get_response(request)
        return response