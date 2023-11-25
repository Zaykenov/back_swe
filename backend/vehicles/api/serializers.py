from rest_framework import serializers
from ..models import Vehicle, AuctionVehicle
from drivers.api.serializers import DriverSerializer
from drivers.models import Driver


class VehicleSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    driver_id = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "model",
            "driver",
            "year",
            "fuel_amount",
            "mileage",
            "license_plate",
            "sitting_capacity",
            "driver_id",
        ]

    def create(self, validated_data):
        driver_id = validated_data.pop("driver_id")
        vehicle_driver = Driver.objects.get(pk=driver_id)
        vehicle = Vehicle.objects.create(driver=vehicle_driver, **validated_data)
        return vehicle


class AuctionVehicleSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    license_plate = serializers.CharField(write_only=True)

    class Meta:
        model = AuctionVehicle
        fields = ["id", "vehicle", "images", "status", "information", "license_plate"]

    def create(self, validated_data):
        license_plate = validated_data.pop("license_plate")
        vehicle = Vehicle.objects.get(license_plate=license_plate)
        auction = AuctionVehicle.objects.create(vehicle=vehicle, **validated_data)
        return auction
