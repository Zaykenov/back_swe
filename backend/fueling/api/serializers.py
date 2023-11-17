from django.db import IntegrityError
from rest_framework import serializers
from ..models import FuelingPersonnel, GasFueling
from vehicles.api.serializers import VehicleSerializer
from vehicles.models import Vehicle


class FuelingPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelingPersonnel
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
            instance = FuelingPersonnel.objects.create(**validated_data)
            instance.user_type = "fueling"
            instance.set_password(password)
            instance.save()

        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            raise serializers.ValidationError({"email": ["exists"]})
        return instance


class GasFuelingSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    fueling_person = FuelingPersonnelSerializer(read_only=True)

    personal_id = serializers.PrimaryKeyRelatedField(
        queryset=FuelingPersonnel.objects.all(),
        write_only=True,
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(),
        write_only=True,
    )

    class Meta:
        model = GasFueling
        fields = (
            "vehicle",
            "fueling_person",
            "date_and_time",
            "amount_of_fuel",
            "image_proof",
            "personal_id",
            "vehicle_id",
        )

    def create(self, validated_data):
        vehicle_id = validated_data.pop("vehicle_id")
        personal_id = validated_data.pop("personal_id")
        fueling_person = FuelingPersonnel.objects.get(pk=personal_id)
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        fueling = GasFueling.objects.create(
            fueling_person=fueling_person, vehicle=vehicle, **validated_data
        )
        return fueling
