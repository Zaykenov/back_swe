from rest_framework import permissions


class IsFueling(permissions.BasePermission):
    message = "You are not fueling person."

    def has_permission(self, request, view):
        return request.user.user_type == "fueling" or request.user.is_staff
