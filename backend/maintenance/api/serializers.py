from django.db import IntegrityError
from rest_framework import serializers
from ..models import JobAssignment, RepairingPart, MaintenancePersonnel
from vehicles.api.serializers import VehicleSerializer


class MaintenancePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenancePersonnel
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
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
            instance = MaintenancePersonnel.objects.create(**validated_data)
            instance.user_type = "maintenance"
            instance.set_password(password)
            instance.save()

        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            raise serializers.ValidationError({"email": ["exists"]})
        return instance


class RepairingPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairingPart
        fields = "__all__"


class JobAssignmentSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    repairing_parts = RepairingPartSerializer(many=True, read_only=True)

    class Meta:
        model = JobAssignment
        fields = "__all__"

