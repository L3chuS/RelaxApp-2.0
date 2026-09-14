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
    
    email = serializers.EmailField()
    code = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    
    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError({
                "password_no_match": "Passwords do not match."
            })
        return data
