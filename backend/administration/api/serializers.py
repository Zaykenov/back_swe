from rest_framework import serializers
from vehicles.api.serializers import VehicleSerializer
from ..models import VehicleReport
from vehicles.models import Vehicle
from fueling.models import GasFueling
from maintenance.models import JobAssignment
from fueling.api.serializers import GasFuelingSerializer
from maintenance.api.serializers import JobAssignmentSerializer

class VehicleReportSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    fueling = GasFuelingSerializer(read_only = True)
    maintenance = JobAssignmentSerializer(read_only = True)

    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), write_only=True
    )

    class Meta:
        model = VehicleReport
        fields = (
            "id",
            "vehicle",
            "vehicle_id",
            "fueling",
            "maintenance",
            "start_date",
            "end_date",
        )

    def create(self, validated_data):
        vehicle_id = validated_data.pop("vehicle_id")
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        fueling = GasFueling.objects.get(vehicle=vehicle)
        maintenance = JobAssignment.objects.get(vehicle=vehicle)
        report = VehicleReport.objects.create(
            vehicle=vehicle, fueling=fueling, maintenance=maintenance, **validated_data
        )
        return report
