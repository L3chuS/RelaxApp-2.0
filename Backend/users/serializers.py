# External imports.
from rest_framework import serializers

# Internal imports.
from .models import Profiles

class UserLoginSerializer(serializers.Serializer):
    """Validate the data required for user authentication."""
    
    username = serializers.CharField()
    password = serializers.CharField()
    

class UserRegistrationSerializer(serializers.Serializer):
    """Validate the data required for user registration."""
    
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField()


class UserChangePasswordSerializer(serializers.Serializer):
    """Validate the data required to request a password reset."""
    
    email = serializers.EmailField()

  
class UserChangePasswordConfirmationSerializer(serializers.Serializer):
    """Validate the data required to request a password reset."""
    
    email = serializers.EmailField()
    code = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    
    def validate(self, data):
        """This function validates that both passwords match."""
        
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError({
                "PASSWORD_NO_MATCH": "Passwords do not match."
            }) 
        return data


class ProfilesSerializer(serializers.ModelSerializer):
    """Validate the data required to set a profile."""
    
    class Meta:
        model = Profiles
        fields = [
            "id",
            "profile_name",
            "visual_configuration",
            "stretch_configuration",
            "final_sounds_configuration",
            "lapse_sounds_configuration",
            "default_profile"
        ]
    
    def validate(self, data):
        """This function validates the the value configuration to prevent both from being empty."""
        
        if (
            data.get("visual_configuration", "") == ""
            and data.get("stretch_configuration", "") == ""
        ):
            raise serializers.ValidationError({
                "PROFILE_VALUES_EMPTY": "Visual Configuration and Stretch Configuration can't both be empty."
            })

        return data