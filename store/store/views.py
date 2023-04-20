from rest_framework.views import APIView
from rest_framework.response import Response

from helpers.permissions import IsBSAuthenticated

# Create your views here.


class TestAPIView(APIView):
    permission_classes = [IsBSAuthenticated, ]

    def get(self, request):
        print("View", request.bs_auth)
        return Response({"message": "Hello, world!"})

    def post(self, request):
        return Response({"message": "Hello, world!"})

    def put(self, request):
        return Response({"message": "Hello, world!"})

    def patch(self, request):
        return Response({"message": "Hello, world!"})

    def delete(self, request):
        return Response({"message": "Hello, world!"})
    