from django.urls import path
from .views import driver_dispatcher_room, DispatcherRegistrationView

urlpatterns = [
    path('chat/<int:user_id>/', driver_dispatcher_room, name='driver_dispatcher_room'),
    path('dispatcher/create/', DispatcherRegistrationView.as_view(), name='dispathcer-create')
]
