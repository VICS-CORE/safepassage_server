from rest_framework import permissions

from passsystem import views
from passsystem.models import User


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # allow login and logout requests without authentication
        if isinstance(view, views.SessionLoginApiView) or isinstance(view, views.SessionLogoutApiView)\
                or isinstance(view, views.create_token_uid):
            return True

        # Otherwise, only allow authenticated requests
        return request.user is not None and isinstance(request.user, User)
