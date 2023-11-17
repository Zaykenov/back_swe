from rest_framework import serializers
from vehicles.api.serializers import VehicleSerializer
from ..models import VehicleReport
from vehicles.models import Vehicle

class VehicleReportSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only = True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset = Vehicle.objects.all(),
        write_only = True)

    class Meta:
        model = VehicleReport
        fields = ('id', 'vehicle', 'vehicle_id', 'vehicle_performance', 'fuel_performance', 'maintenance_performance')

    def create(self, validated_data):
        vehicle_id = validated_data.pop("vehicle_id")
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        report = VehicleReport.objects.create(vehicle=vehicle, **validated_data)
        return report