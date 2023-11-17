from django.db import models
from vehicles.models import Vehicle
from accounts.models import CustomUser

class MaintenancePersonnel(CustomUser):
    
    def __str__(self) -> str:
        return self.email

class JobAssignment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    maintenance_cost = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.date}"


class RepairingPart(models.Model):
    job_assignment = models.ForeignKey(JobAssignment, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=50)
    part_condition = models.TextField()
    part_image = models.ImageField(upload_to="part_images/")

    def __str__(self):
        return f"{self.job_assignment.vehicle.license_plate} - {self.part_number}"
