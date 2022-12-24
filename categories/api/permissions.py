from rest_framework.permissions import BasePermission

class IsAdminOrReadOnlyPermission(BasePermission):
    def has_permisions(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
        
    