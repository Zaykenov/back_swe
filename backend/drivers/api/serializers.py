from django.db import IntegrityError
from rest_framework import serializers
from ..models import Driver, Route
from accounts.models import CustomUser
from accounts.api.serializers import UserSerializer


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "government_id",
            "address",
            "phone_number",
            "driving_license_code",
            "password",
            "user_type",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "user_type": {"write_only": False, "read_only": False},
        }

    def create(self, validated_data):
        try:
            password = validated_data.pop("password")
            instance = Driver.objects.create(**validated_data)
            instance.user_type = "driver"
            instance.set_password(password)
            instance.save()

        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            raise serializers.ValidationError({"email": ["exists"]})
        return instance


class RouteSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)

    class Meta:
        model = Route
        fields = (
            "client",
            "name",
            "description",
            "start_position",
            "end_position",
            "status_route",
        )
        extra_kwargs = {"status_route": {"read_only": True}}


class RouteUpdateSerializer(serializers.ModelSerializer):
    assigned_driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Route
        fields = (
            "id",
            "name",
            "description",
            "start_position",
            "end_position",
            "assigned_driver",
            "driver_id",
            "status_route",
        )
    def update(self, instance, validated_data):
        driver_id = validated_data.get('driver_id')
        status_route = validated_data.get('status_route')
        if driver_id:
            assigned_driver = Driver.objects.get(pk = driver_id)
            instance.assigned_driver = assigned_driver
        if status_route:
            instance.status_route = status_route
        instance.save()
        return instance
