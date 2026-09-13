from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """Проверка аутентификации пользователя."""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Проверка прав доступа к объекту:
        чтение - всем, запись - только автор."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
