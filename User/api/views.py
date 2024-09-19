
from User.models import User
from User.api.serializers import UserSerializer,UserPermissionSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import mixins, viewsets
from User.models import User
from rest_framework import status
from rest_framework.response import Response


class UserViewSet(
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer



    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

class UserPermissionViewSet(
                   #mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserPermissionSerializer
    #permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Verilerin işlenmesi ve güncellenmesi
        return super().update(request, *args, **kwargs)