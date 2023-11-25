from django.db import models
from vehicles.models import Vehicle


class VehicleReport(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.vehicle.license_plate

    