from rest_framework import serializers
from .models import Profiles

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
    

# class ProfilesSerializer(serializers.Serializer):
#     profile_name = serializers.CharField()
#     visual_configuration = serializers.CharField(
#         required=False,
#         allow_blank=True
#     )
#     stretch_configuration = serializers.CharField(
#         required=False,
#         allow_blank=True
#     )
#     final_sounds_configuration = serializers.CharField(
#         required=False,
#         allow_blank=True
#     )
#     lapse_sounds_configuration = serializers.CharField(
#         required=False,
#         allow_blank=True
#     )
    
#     def validate(self, data):
#         if data["visual_configuration"] == "" and data["stretch_configuration"] == "":
#             raise serializers.ValidationError({
#                 "PROFILE_VALUES_EMPTY": "Visual Configuration and Stretch Configuration can't both be empty."
#             }) 
#         return data

class ProfilesSerializer(serializers.ModelSerializer):
    
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
        if (
            data.get("visual_configuration", "") == ""
            and data.get("stretch_configuration", "") == ""
        ):
            raise serializers.ValidationError({
                "PROFILE_VALUES_EMPTY": "Visual Configuration and Stretch Configuration can't both be empty."
            })

        return data