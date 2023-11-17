from rest_framework import permissions


class IsMaintenance(permissions.BasePermission):
    message = "You are not the a maintenance person."

    def has_permission(self, request, view):
        return request.user.user_type == "driver" or request.user.is_staff
