from accounts.models import CustomUser
from django.db import models


class Route(models.Model):
    STATUS_CHOICES = [
        ("not_completed", "Not Completed"),
        ("canceled", "Canceled"),
        ("delayed", "Delayed"),
        ("completed", "Completed"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_position = models.CharField(max_length=255)
    end_position = models.CharField(max_length=255)
    assigned_driver = models.ForeignKey(
        "Driver", on_delete=models.CASCADE, related_name="assigned_routes"
    )
    status = models.CharField(
        max_length=20, blank=True, null=True, choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.name


class Driver(CustomUser):
    government_id = models.CharField(max_length=20)
    driving_license_code = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.email
