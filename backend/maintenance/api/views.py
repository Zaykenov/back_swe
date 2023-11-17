from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from ..models import JobAssignment, RepairingPart, MaintenancePersonnel
from .serializers import (
    JobAssignmentSerializer,
    RepairingPartSerializer,
    MaintenancePersonnelSerializer,
)
from vehicles.models import Vehicle
from vehicles.api.serializers import VehicleSerializer
from .permissions import IsMaintenance


@extend_schema(tags=["Vehicle"])
class VehicleDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsMaintenance]


@extend_schema(tags=["Maintenance"])
class MaintenancePersonnelRegisterView(generics.ListCreateAPIView):
    queryset = MaintenancePersonnel.objects.all()
    serializer_class = MaintenancePersonnelSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Maintenance"])
class JobAssignmentListView(generics.ListAPIView):
    queryset = JobAssignment.objects.all()
    serializer_class = JobAssignmentSerializer
    permission_classes = [IsMaintenance]


@extend_schema(tags=["Maintenance"])
class JobAssignmentCreateView(generics.CreateAPIView):
    queryset = JobAssignment.objects.all()
    serializer_class = JobAssignmentSerializer
    permission_classes = [IsMaintenance]


@extend_schema(tags=["Maintenance"])
class RepairingPartListView(generics.ListAPIView):
    queryset = RepairingPart.objects.all()
    serializer_class = RepairingPartSerializer
    permission_classes = [IsMaintenance]


@extend_schema(tags=["Maintenance"])
class RepairingPartCreateView(generics.CreateAPIView):
    queryset = RepairingPart.objects.all()
    serializer_class = RepairingPartSerializer
    permission_classes = [IsMaintenance]
