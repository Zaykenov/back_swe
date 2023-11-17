# drivers/urls.py
from django.urls import path
from .views import (
    DriverDetailView,
    AssignedRouteListView,
    ActiveRouteView,
    ChangeRouteStatusView,
    CompletedRouteHistoryView,
    DriverRegistrationView,
    RouteCreateView,
    RouteDetailView
)

urlpatterns = [
    path('<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
    path('register/', DriverRegistrationView.as_view(), name = 'drver-regster'),
    path('assigned-routes/', AssignedRouteListView.as_view(), name='assigned-routes-list'),
    path('active-route/', ActiveRouteView.as_view(), name='active-route'),
    path('change-route-status/<int:pk>/', ChangeRouteStatusView.as_view(), name='change-route-status'),
    path('completed-route-history/', CompletedRouteHistoryView.as_view(), name='completed-route-history'),
    path('route/create/', RouteCreateView.as_view(), name='route-create'),
    path('route/<int:pk>/', RouteDetailView.as_view(), name = 'route-detail')
]
