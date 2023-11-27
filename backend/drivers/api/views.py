from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Driver, Route
from .serializers import DriverSerializer, RouteSerializer, RouteUpdateSerializer
from drf_spectacular.utils import extend_schema
from .permissions import IsAssignedDriver, IsDriver, IsOwner


@extend_schema(tags=["Driver"])
class DriverRegistrationView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Driver"])
class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAssignedDriver, permissions.IsAdminUser]
    lookup_field = "pk"


@extend_schema(tags=["Route"])
class AwaitingRouteView(generics.ListAPIView):
    queryset = Route.objects.filter(status_route="awaiting")
    serializer_class = RouteUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema(tags=["Route"])
class AwaitingRouteDetailView(generics.RetrieveUpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteUpdateSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()


@extend_schema(tags=["Route"])
class AssignedRouteListView(generics.ListAPIView):
    serializer_class = RouteUpdateSerializer
    permission_classes = [IsDriver]

    def get_queryset(self):
        driver = self.request.user
        return Route.objects.filter(assigned_driver=driver.id, status_route="awaiting")


@extend_schema(tags=["Route"])
class ActiveRouteView(generics.ListAPIView):
    serializer_class = RouteUpdateSerializer
    permission_classes = [IsDriver]

    def get_queryset(self):
        driver = self.request.user
        return Route.objects.filter(assigned_driver=driver.id, status_route="active")


@extend_schema(tags=["Route"])
class ChangeRouteStatusView(generics.RetrieveUpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteUpdateSerializer
    permission_classes = [IsAssignedDriver]
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()


@extend_schema(tags=["Route"])
class CompletedRouteHistoryView(generics.ListAPIView):
    serializer_class = RouteUpdateSerializer
    permission_classes = [IsDriver]

    def get_queryset(self):
        driver = self.request.user
        return Route.objects.filter(assigned_driver=driver.id, status_route="completed")


@extend_schema(tags=["Route"])
class RouteCreateView(generics.CreateAPIView):
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        client = self.request.user
        return Route.objects.filter(client=client)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user, status_route="awaiting")


@extend_schema(tags=["Route"])
class RouteDetaiUserView(generics.RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsOwner]
