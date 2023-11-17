from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Driver, Route
from .serializers import DriverSerializer, RouteSerializer
from drf_spectacular.utils import extend_schema
from .permissions import IsAssignedDriver, IsDriver


@extend_schema(tags=["Driver"])
class DriverRegistrationView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Driver"])
class DriverDetailView(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAssignedDriver]
    lookup_field = "pk"


@extend_schema(tags=["Route"])
class RouteDetailView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAssignedDriver]
    lookup_field = "pk"


@extend_schema(tags=["Route"])
class RouteCreateView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Route"])
class AssignedRouteListView(generics.ListAPIView):
    serializer_class = RouteSerializer
    permission_classes = [IsDriver]

    def get_queryset(self):
        driver = self.request.user
        return Route.objects.filter(assigned_driver=driver.id)


@extend_schema(tags=["Route"])
class ActiveRouteView(generics.ListAPIView):
    serializer_class = RouteSerializer
    permission_classes = [IsDriver]

    def get_queryset(self):
        driver = self.request.user
        return Route.objects.filter(assigned_driver=driver.id, status="not_completed")


@extend_schema(tags=["Route"])
class ChangeRouteStatusView(generics.UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAssignedDriver]
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data.get("status", instance.status)
        instance.save()

        return Response(status=status.HTTP_200_OK)


@extend_schema(tags=["Route"])
class CompletedRouteHistoryView(generics.ListAPIView):
    serializer_class = RouteSerializer
    permission_classes = [IsDriver]

    def get_queryset(self):
        driver = self.request.user
        return Route.objects.filter(assigned_driver=driver.id, status="completed")
