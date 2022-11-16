from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            "password": {"write_only": True, "required": True},
            "email": {"required": True},
            "is_active": {"default": True},
        }

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, required=True)
    class Meta: 
        model=User
        fields=['username', 'password']