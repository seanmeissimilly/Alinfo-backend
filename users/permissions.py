from rest_framework import permissions

# clases de permisos


class IsAdmin(permissions.BasePermission):
    # Permiso para los usuarios con rol de administrador
    def has_permission(self, request, view):
        return request.user and request.user.role == "admin"


class IsEditor(permissions.BasePermission):
    # Permiso para los usuarios con rol de editor
    def has_permission(self, request, view):
        return request.user and request.user.role == "editor"


class IsReader(permissions.BasePermission):
    # Permiso para los usuarios con rol de reader
    def has_permission(self, request, view):
        return request.user and request.user.role == "reader"
