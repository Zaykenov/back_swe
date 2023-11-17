from django.urls import path
from .views import (
    VehicleDetailUpdateView,
    JobAssignmentListView,
    JobAssignmentCreateView,
    RepairingPartListView,
    RepairingPartCreateView,
    MaintenancePersonnelRegisterView
)

urlpatterns = [
    path('vehicles/<int:pk>/', VehicleDetailUpdateView.as_view(), name='vehicle-detail-update'),
    path('job-assignments/', JobAssignmentListView.as_view(), name='job-assignment-list'),
    path('job-assignments/create/', JobAssignmentCreateView.as_view(), name='job-assignment-create'),
    path('repairing-parts/', RepairingPartListView.as_view(), name='repairing-part-list'),
    path('repairing-parts/create/', RepairingPartCreateView.as_view(), name='repairing-part-create'),
    path('maintenance/register/', MaintenancePersonnelRegisterView.as_view(), name= 'maintenance-register')
]