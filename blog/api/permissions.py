from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadonly(BasePermission):
    message = "You must be owner of this  object."
    def has_permission(self, request, view):
        my_safe_method = ['GET', 'PUT', 'DELETE']
        if request.method in my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff
