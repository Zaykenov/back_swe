from django.urls import path
from .views import (
    ReportCreateView,
    ReportListView
)

urlpatterns = [
    path("reports/", ReportListView.as_view(), name="report-list"),
    path("reports/create/", ReportCreateView.as_view(), name="report-create"),
]
