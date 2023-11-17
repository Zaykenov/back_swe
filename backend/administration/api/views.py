from rest_framework import generics
from rest_framework import permissions
from drf_spectacular.utils import extend_schema
from ..models import VehicleReport
from .serializers import VehicleReportSerializer


@extend_schema(tags=["Report"])
class ReportListView(generics.ListAPIView):
    queryset = VehicleReport.objects.all()
    serializer_class = VehicleReportSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Report"])
class ReportCreateView(generics.CreateAPIView):
    queryset = VehicleReport.objects.all()
    serializer_class = VehicleReportSerializer
    permission_classes = [permissions.IsAdminUser]