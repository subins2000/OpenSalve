from accounts.models import User
from rest_framework import permissions


class IsVolunteer(permissions.BasePermission):
    """Custom permission to only allow volunteers to edit requests
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        user = User.objects.get(username=request.user.username)

        return user.role == 'volunteer' or user.role == 'admin'
