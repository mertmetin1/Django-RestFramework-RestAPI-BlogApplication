from rest_framework import permissions




class IsBlogAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit or delete.
    Non-admin users can only perform read-only actions.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        if request.user.is_staff:
            return True
         
        if request.user.is_superuser:
            return True
        # Admin users have all permissions (GET, POST, PUT, DELETE, etc.)
        if request.user.İs_blogAdmin:
            return True
        
        # For non-admin users, only allow safe methods (GET, HEAD, OPTIONS)
        return request.method in permissions.SAFE_METHODS