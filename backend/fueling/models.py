from django.db import models
from vehicles.models import Vehicle
from accounts.models import CustomUser


class FuelingPersonnel(CustomUser):
    def __str__(self) -> str:
        return self.email


class GasFueling(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fueling_person = models.ForeignKey(FuelingPersonnel, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    amount_of_fuel = models.FloatField()
    image_proof = models.ImageField(upload_to="image_proof/")

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.date_and_time}"
