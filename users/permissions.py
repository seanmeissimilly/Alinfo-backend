from rest_framework.permissions import BasePermission

# Clases de permisos


class IsAdmin(BasePermission):
    # Permiso para los usuarios con rol de administrador
    def has_permission(self, request, view):
        return request.user and request.user.role == "admin"


class IsEditor(BasePermission):
    # Permiso para los usuarios con rol de editor
    def has_permission(self, request, view):
        return request.user and request.user.role == "editor"


class IsReader(BasePermission):
    # Permiso para los usuarios con rol de reader
    def has_permission(self, request, view):
        return request.user and request.user.role == "reader"


class IsAdminOrIsEditorAndOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permitir acceso si el usuario es administrador
        if request.user.role == "admin":
            return True
        # Permitir acceso si el usuario es editor y es el propietario del documento
        if request.user.role == "editor" and obj.user == request.user:
            return True
        return False


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permitir acceso si el usuario es administrador o el propietario del objeto
        return request.user.role == "admin" or obj.user == request.user
