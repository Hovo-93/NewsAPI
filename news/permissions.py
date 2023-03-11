from rest_framework import permissions
from rest_framework.permissions import BasePermission
from news.models import UserRoles


class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_superuser or request.user.role == UserRoles.ADMIN
        )


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHOD:
            return True
        return obj.author == request.user  # obj.user bazai userne


class IsNewsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE']:
            return obj.news.author == request.user
