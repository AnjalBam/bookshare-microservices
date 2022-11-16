from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, viewsets

from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings

from .serializers import UserSerializer, LoginSerializer

client = settings.REDIS_INSTANCE
User = get_user_model()


# Create your views here.
@api_view(["GET"])
def test(request, *args, **kwargs):
    client.set("name", "Anjal")
    name = client.get("name")
    print(name)
    return Response({"url": request.path, "name": name})


class SignUpAPIView(APIView):
    model = User
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.POST)
        print(User)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data.get("password", None))

        user = serializer.save()
        user.set_password(serializer.validated_data.get("password", None))
        user.is_active = True
        user.save()
        return Response(
            {"message": "User signed up successfully"}, status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    model = User
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.POST)

        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if not user:
            return Response(
                {
                    "message": "Login Failed. Invalid Credentials",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        refresh = RefreshToken.for_user(user)

        access_token = str(refresh.access_token)

        client.hset(access_token, mapping={"user": user.id})

        return Response(
            {
                "message": "User logged in successfully",
                "data": {"token": access_token},
            },
            status=status.HTTP_200_OK,
        )
