from rest_framework import serializers
from rest_framework.authtoken.models import Token
from User.models import User
from rest_framework.response import Response
from rest_framework import  status
from django.contrib.auth.models import Permission

from rest_framework import serializers
from User.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(max_length=15)
    phone_code = serializers.CharField(max_length=5)
    user_permissions = serializers.SerializerMethodField()  
    


    class Meta:
        model = User
        fields = ['id','user_permissions', 'first_name','username', 'last_name', 'password', 'password_confirmation', 'phone_number', 'phone_code', 'email', 'date_joined', 'is_active','groups']
    
    def validate(self, data):
        if data.get('password') != data.get('password_confirmation'):
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')  # Remove password_confirmation from validated_data
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    
    def update(self, instance, validated_data):
        validated_data.pop('password_confirmation', None)  # Remove password_confirmation from validated_data
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def get_user_permissions(self, obj):
        request = self.context.get('request')
        if request and request.user.has_perm('view_user_permissions'):
            return [perm.codename for perm in obj.user_permissions.all()]
        return []

    
class UserPermissionSerializer(serializers.ModelSerializer):
    username=serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','user_permissions']
        #fields='__all__'
   
    def update(self, instance, validated_data):
        permissions = validated_data.pop('user_permissions', None)
        if permissions is not None:
            instance.user_permissions.set(permissions)
        return super().update(instance, validated_data)