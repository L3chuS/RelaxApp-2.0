from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .serializers import *

@api_view(["POST"])
def user_login(request):
    
    login_serializer = UserLoginSerializer(data=request.data)
    
    if login_serializer.is_valid():
        username = login_serializer.validated_data["username"]
        password = login_serializer.validated_data["password"]
        
        user = User.objects.filter(username=username).first()
             
        if user is None:
            return Response(
                {"error" : "User does not exists.",
                 "error_type" : "VIEWS",
                 "error_link" : "ERROR_LOGIN_USERNAME_NOT_EXISTS"},
                status=401
            )
            
        if not user.check_password(password):
            return Response(
                {"error" : "Invalid Password.",
                 "error_type" : "VIEWS",
                 "error_link" : "ERROR_LOGIN_INVALID_PASSWORD"},
                status=401
            )
        
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response(
            {"message" : "Logging in.",
             "username" : user.username,
             "token" : token.key,
             "message_type" : "MESSAGE_LOGIN_CORRECT"}
            )
    else:
        #serializer_error_message = next(iter(login_serializer.errors.values()))[0]
        return Response(
            {"error" : login_serializer.errors,
             "error_type" : "SERIALIZER",
             "error_link" : "ERROR_SERIALIZER_GENERAL"}, 
            status=400
            )

@api_view(["POST"])
def user_registration(request):
    
    register_serializer = UserRegistrationSerializer(data=request.data)
    
    if register_serializer.is_valid():
        first_name = register_serializer.validated_data["first_name"]
        last_name = register_serializer.validated_data["last_name"]
        username = register_serializer.validated_data["username"]
        email = register_serializer.validated_data["email"]
        password = register_serializer.validated_data["password"]

        username_exist = User.objects.filter(username=username).exists()
        email_exist = User.objects.filter(email=email).exists()
        
        if username_exist:
            return Response(
                {"error" : "Username already exists.",
                 "error_type" : "VIEWS",
                 "error_link" : "ERROR_REGISTER_USERNAME_EXISTS"},
                status=400
            )
            
        elif email_exist:
            return Response(
                {"error" : "Email already exists.",
                 "error_type" : "VIEWS",
                 "error_link" : "ERROR_REGISTER_EMAIL_EXISTS"},
                status=400
            )
        
        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        return Response(
            {"message" : "Registration user.",
             "first_name" : first_name,
             "last_name" : last_name,
             "username" : username,
             "email" : email,
             "message_type" : "MESSAGE_REGISTER_USER_CREATED"
            },
            status=201
        )
    
    else:
        #serializer_error_message = next(iter(register_serializer.errors.values()))[0]
        return Response({
            "error" : register_serializer.errors,
            "error_type" : "SERIALIZER",
            "error_link" : "ERROR_SERIALIZER_GENERAL"}, 
            status=400
        )