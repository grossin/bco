from rest_framework.permissions import BasePermission
from .models import User

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User):
            return obj.owner == request.user
        return obj.owner == request.user