from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from ..models import GasFueling, FuelingPersonnel
from .serializers import GasFuelingSerializer, FuelingPersonnelSerializer
from .permissions import IsFueling

@extend_schema(tags=["Fueling"])
class FuelingRegisterView(generics.ListCreateAPIView):
    queryset = FuelingPersonnel.objects.all()
    serializer_class = FuelingPersonnelSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Fueling"])
class GasFuelingListCreateView(generics.ListCreateAPIView):
    queryset = GasFueling.objects.all()
    serializer_class = GasFuelingSerializer
    permission_classes = [IsFueling]


@extend_schema(tags=["Fueling"])
class GasFuelingRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = GasFueling.objects.all()
    serializer_class = GasFuelingSerializer
    permission_classes = [IsFueling]
