from rest_framework import serializers

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
                "PASSWORD_NO_MATCH": "Passwords do not match."
            }) 
        return data
    

class ProfilesSerializer(serializers.Serializer):
    profile_name = serializers.CharField()
    visual_configuration = serializers.CharField(
        required=False,
        allow_blank=True
    )
    stretch_configuration = serializers.CharField(
        required=False,
        allow_blank=True
    )
    final_sounds_configuration = serializers.CharField(
        required=False,
        allow_blank=True
    )
    lapse_sounds_configuration = serializers.CharField(
        required=False,
        allow_blank=True
    )
