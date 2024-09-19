from rest_framework import mixins
from Blog.models import Blog


from rest_framework import mixins, viewsets
from Blog.api.serializers import BlogSerializer
from Blog.api.permissions import IsBlogAdminOrReadOnly
from rest_framework import status
from rest_framework.response import Response

class BlogViewSet(
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    
    queryset = Blog.objects.filter(IsDeleted=False)
    serializer_class = BlogSerializer
    permission_classes=[IsBlogAdminOrReadOnly]
    
    
    
    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.IsDeleted = True
        blog.save()
        return Response(status=status.HTTP_204_NO_CONTENT)