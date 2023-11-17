from django.db import models
from vehicles.models import Vehicle



class VehicleReport(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_performance = models.TextField()
    fuel_performance = models.TextField()
    maintenance_performance = models.TextField()

    def __str__(self) -> str:
        return self.vehicle.license_plate

    