from django.urls import path
from .views import GasFuelingListCreateView, GasFuelingRetrieveUpdateView, FuelingRegisterView

urlpatterns = [
    path('gas-fueling/', GasFuelingListCreateView.as_view(), name='gas-fueling-list-create'),
    path('gas-fueling/<int:pk>/', GasFuelingRetrieveUpdateView.as_view(), name='gas-fueling-retrieve-update'),
    path('fueling-personnel/register/', FuelingRegisterView.as_view(), name='fueling-personnel-register'),
]
