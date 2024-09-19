from rest_framework import serializers
from Blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    IsDeleted=serializers.BooleanField(read_only=True)
    isGenByAi=serializers.BooleanField(read_only=True)

    
    class Meta:
        model = Blog
        fields='__all__'
        
        
