from rest_framework.permissions import BasePermission


class IsBSAuthenticated(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.bs_auth['is_authenticated']:
                return True
        except:
            return False

