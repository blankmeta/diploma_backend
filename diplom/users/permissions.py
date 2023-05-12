from rest_framework.permissions import BasePermission, SAFE_METHODS


class CurrentUserOrReadOnly(BasePermission):
    # def has_permission(self, request, view):
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj:
            return True
        return False
