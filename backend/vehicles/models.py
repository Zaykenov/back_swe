from django.db import models
from drivers.models import Driver


class Vehicle(models.Model):
    active_status= [
        ('active', 'Active'),
        ('non_active', 'Non-Active'),
    ]
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    sitting_capacity = models.PositiveIntegerField()
    mileage = models.FloatField()
    fuel_amount = models.FloatField()
    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vehicles",
    )
    activeness = models.CharField(max_length=20, choices=active_status, default='active')


    def __str__(self):
        return f"{self.year} {self.model} ({self.license_plate})"


class AuctionVehicle(models.Model):
    STATUS_CHOICES = [
        ("not_sold", "Not Sold"),
        ("sold", "Sold"),
    ]
    vehicle = models.OneToOneField(
        Vehicle, on_delete=models.CASCADE, related_name="auction"
    )
    images = models.ImageField(upload_to="auction_images/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    information = models.TextField()

    def __str__(self):
        return f"Auction for {self.vehicle}"
