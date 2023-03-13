from rest_framework import permissions
from rest_framework.permissions import BasePermission
from news.models import UserRoles, News


class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_superuser or request.user.role == UserRoles.ADMIN
        )


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHOD:
            return True
        return obj.author == request.user


class IsNewsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE']:
            return obj.news.author == request.user


class IsLikedNews(BasePermission):
    message = 'You have already liked this news'

    def has_permission(self, request, view):
        if request.method == 'POST':
            user = request.user
            news_id = view.kwargs.get('pk')
            news = News.objects.get(id=news_id)
            return not news.like_set.filter(user=user).exists()
        return True
