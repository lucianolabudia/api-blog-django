from rest_framework.permissions import BasePermission


# Si es Administrador va a poder hacer de todo, sino, solo va a poder leer
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            # solo usuarios q sean miembros del staff van a poder ejecutar la epticion
            return request.user.is_staff
        