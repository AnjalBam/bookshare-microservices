import jwt
from django.conf import settings

class BSAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def jwt_decode(self, token):
        decoded = jwt.decode(
            token,
            key=settings.JWT_SIGNING_KEY,
            algorithms=[
                "HS256",
            ],
        )
        return decoded

    def __call__(self, request):
        jwt_token = request.headers.get('Authorization').split()[-1]
        auth_status = {
            "is_authenticated": False,
            "user": None
        }
        if jwt_token:
            try:
                payload = self.jwt_decode(jwt_token)
                auth_status['is_authenticated'] = True
                auth_status['user'] = payload
            except Exception as e:
                pass
        request.bs_auth = auth_status

        return self.get_response(request)