from rest_framework import serializers
#from django.contrib.auth.models import User

class UserLoginSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField()
    

class UserRegistrationSerializer(serializers.Serializer):
    
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

class UserChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class UserChangePasswordConfirmationSerializer(serializers.Serializer):
    code = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()