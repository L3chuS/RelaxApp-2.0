from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import secrets
import resend
import base64
from django.conf import settings
from .models import *
from .serializers import *


@api_view(["POST"])
def user_login(request):
    
    login_serializer = UserLoginSerializer(data=request.data)
    
    if login_serializer.is_valid():
        username = login_serializer.validated_data["username"]
        password = login_serializer.validated_data["password"]
        
        user = User.objects.filter(username=username).first()
        
    else:
        return Response(
            {"error" : login_serializer.errors,
            "error_type" : "SERIALIZERS",
            "error_link" : "ERROR_SERIALIZERS_GENERAL"}, 
            status=400
            )
             
    if user is None:
        return Response(
            {"error" : "* ERROR: User does not exists.",
            "error_type" : "VIEWS",
            "error_link" : "ERROR_LOGIN_USERNAME_NOT_EXISTS"},
            status=401
        )

    if not user.check_password(password):
        return Response(
            {"error" : "* ERROR: Invalid Password.",
            "error_type" : "VIEWS",
            "error_link" : "ERROR_LOGIN_INVALID_PASSWORD"},
            status=401
        )
    
    Token.objects.filter(user=user).delete()
    token = Token.objects.create(user=user)
    return Response(
        {"message" : "* MESSAGE: Logging in.",
        "username" : user.username,
        "token" : token.key,
        "message_link" : "MESSAGE_LOGIN_CORRECT"}
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
        
    else:
        return Response({
            "error" : register_serializer.errors,
            "error_type" : "SERIALIZERS",
            "error_link" : "ERROR_SERIALIZERS_GENERAL"}, 
            status=400
        )
    
    if username_exist:
        return Response(
            {"error" : "* ERROR: Username already exists.",
            "error_type" : "VIEWS",
            "error_link" : "ERROR_REGISTER_USERNAME_EXISTS"},
            status=400
        )
        
    elif email_exist:
        return Response(
            {"error" : "* ERROR: Email already exists.",
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
        {"message" : "* MESSAGE: User has been registered.",
        "first_name" : first_name,
        "last_name" : last_name,
        "username" : username,
        "email" : email,
        "message_link" : "MESSAGE_REGISTER_USER_CREATED"
        },
        status=201
    )


@api_view(["POST"])     
def user_pw_reset(request):
    change_pw_serializer = UserChangePasswordSerializer(data=request.data)
    
    if change_pw_serializer.is_valid():
        email = change_pw_serializer.validated_data["email"]

        user = User.objects.filter(email=email).first()
    
    else:
        return Response({
            "error" : change_pw_serializer.errors,
            "error_type" : "SERIALIZERS",
            "error_link" : "ERROR_SERIALIZERS_GENERAL"}, 
            status=400
        )    
        
    if user is None:
        return Response({
            "message" : "* MESSAGE: If the email is registered, a recovery code has been sent.",
            "message_link" : None}, 
            status=200
        )

    code = str(secrets.randbelow(1000000)).zfill(6)
    
    PasswordReset.objects.filter(user=user).delete()
    PasswordReset.objects.create(
        user = user,
        code = code,
        expires_at=timezone.now() + timedelta(minutes=2)
    )
    
    # It converts the variables at the html.    
    html_content = render_to_string(
        "emails/password_reset.html",
        {
            "user_first_name" : user.first_name,
            "user_last_name" : user.last_name,
            "username" : user.username,
            "code" : code,
        }
    )
    
    logo_path = settings.BASE_DIR / "images" / "Logo.png"
    
    with open(logo_path, "rb") as image_file:
        logo = base64.b64encode(image_file.read()).decode("utf-8")
    
    resend.api_key = settings.RESEND_API_KEY

    resend.Emails.send({
        "from": settings.RESEND_FROM_EMAIL,
        "to": email,
        "subject": "RelaxApp - Código de recuperación",
        "text": f"El código de recuperación es: {code}",
        "html": html_content,
        "attachments": [
            {
                "filename": "Logo.png",
                "content": logo,
                "content_id": "relaxapp_logo",
            }
        ]
    })
       
    return Response({
        "message": "* MESSAGE: If the email is registered, a recovery code has been sent.",
        "message_link" : None},
        status=200)
    
   
@api_view(["PUT"])     
def user_pw_reset_confirmation(request):
    
    change_pw_confirm_serializer =  UserChangePasswordConfirmationSerializer(data=request.data)
    
    if change_pw_confirm_serializer.is_valid():
        email = change_pw_confirm_serializer.validated_data["email"]
        code = change_pw_confirm_serializer.validated_data["code"]
        password1 = change_pw_confirm_serializer.validated_data["password1"]
        
        user = User.objects.filter(email=email).first()
        user_token = PasswordReset.objects.filter(user=user, code=code).first()
    else:
        return Response({
            "error" : change_pw_confirm_serializer.errors,
            "error_type" : "SERIALIZERS",
            "error_link" : "ERROR_SERIALIZERS_GENERAL"}, 
            status=400
        )

    if user_token == None:
        return Response({
            "error" : "* ERROR: Token is incorrect.",
            "error_type" : "VIEWS",
            "error_link" : "ERROR_PW_RESET_CONF_INVALID_TOKEN"}, 
            status=400
        )
        
    if user_token.used:
        return Response({
            "error" : "* ERROR: Token has been used.",
            "error_type" : "VIEWS",
            "error_link" : "ERROR_PW_RESET_CONF_TOKEN_USED"}, 
            status=400
        )
        
    if timezone.now() > user_token.expires_at:
        return Response({
            "error" : "* ERROR: Token has expired.",
            "error_type" : "VIEWS",
            "error_link" : "ERROR_PW_RESET_CONF_TOKEN_EXPIRED"}, 
            status=400
        )
    
    user.set_password(password1)
    user.save()
    
    user_token.used = True
    user_token.save()
    
    return Response(
        {"message" : "* MESSAGE: Password has been updated succesfully.",
        "message_link" : "MESSAGE_PW_RESET_CONF_SUCCESS"},
        status=200
    )