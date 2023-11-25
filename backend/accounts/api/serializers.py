# accounts/serializers.py
from rest_framework import serializers
from ..models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "user_type",
            "iin",
            "phone_number",
            "first_name",
            "last_name",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True},
                        "user_type": {"read_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            user_type="client",
            iin=validated_data.get("iin"),
            phone_number=validated_data.get("phone_number"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}
