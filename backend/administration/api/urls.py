from django.urls import path
from .views import (
    ReportCreateView,
    ReportListView
)

urlpatterns = [
    path("", ReportListView.as_view(), name="report-list"),
    path("create/", ReportCreateView.as_view(), name="report-create"),
]
