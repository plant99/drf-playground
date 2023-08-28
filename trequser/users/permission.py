from rest_framework.permissions import BasePermission


class ViewProfileWithJWTUserPermission(BasePermission):
    message = "Please include JWT in authentication header."
    def has_permission(self, request, _):
        if request.jwt_user:
            return True
        else:
            return False
