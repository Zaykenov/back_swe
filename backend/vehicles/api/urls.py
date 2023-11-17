from django.urls import path
from .views import (
    VehicleListView,
    AuctionVehicleListView,
    VehicleRegisterView,
    AuctionVehicleCreateView,
    AuctionVehicleUpdateView,
)

urlpatterns = [
    path("vehicles/", VehicleListView.as_view(), name="vehicle-list"),
    path("auctions/", AuctionVehicleListView.as_view(), name="auction-list"),
    path("vehicles/create/", VehicleRegisterView.as_view(), name="vehicle-create"),
    path("auctions/create/", AuctionVehicleCreateView.as_view(), name="auction-create"),
    path("auctions/update/<int:pk>/", AuctionVehicleUpdateView.as_view(), name="auction-update"),
]
