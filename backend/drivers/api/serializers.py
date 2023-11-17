from django.db import IntegrityError
from rest_framework import serializers
from ..models import Driver, Route


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
    assigned_driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Route
        fields = (
            "name",
            "description",
            "start_position",
            "end_position",
            "assigned_driver",
            "driver_id",
            "status",
        )

    def create(self, validated_data):
        driver_id = validated_data.pop("driver_id")
        assigned_driver = Driver.objects.get(pk=driver_id)
        route = Route.objects.create(assigned_driver=assigned_driver, **validated_data)
        return route
