from rest_framework import generics
from rest_framework import permissions
from drf_spectacular.utils import extend_schema
from ..models import Vehicle, AuctionVehicle
from .serializers import VehicleSerializer, AuctionVehicleSerializer


@extend_schema(tags=["Vehicle"])
class VehicleListView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Vehicle"])
class VehicleRegisterView(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Auction"])
class AuctionVehicleListView(generics.ListAPIView):
    queryset = AuctionVehicle.objects.all()
    serializer_class = AuctionVehicleSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Auction"])
class AuctionVehicleCreateView(generics.CreateAPIView):
    queryset = AuctionVehicle.objects.all()
    serializer_class = AuctionVehicleSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Auction"])
class AuctionVehicleUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuctionVehicle.objects.all()
    serializer_class = AuctionVehicleSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "pk"
