from rest_framework import permissions


class IsAssignedDriver(permissions.BasePermission):
    message = "You are not the assigned driver for this route."

    def has_permission(self, request, view):
        route = view.get_object()
        return request.user.id == route.assigned_driver.id or request.user.is_staff


class IsDriver(permissions.BasePermission):
    message = "You are not the assigned driver for this route."

    def has_permission(self, request, view):
        return request.user.user_type == "driver"
