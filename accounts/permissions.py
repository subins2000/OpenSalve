from accounts.models import User
from rest_framework import permissions


class IsEditable(permissions.BasePermission):
    """Only allow user and admin to edit their info
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        editing_username = view.kwargs.get(view.lookup_url_kwarg)
        user = User.objects.get(username=request.user.username)

        return user.role == 'admin' or editing_username == user.username
