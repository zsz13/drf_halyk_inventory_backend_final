from rest_framework import permissions


class IsAdmin(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

