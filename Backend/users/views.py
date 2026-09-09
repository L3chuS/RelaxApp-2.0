from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .serializers import UserLoginSerializer

@api_view(["POST"])
def user_login(request):
    
    login_serializer = UserLoginSerializer(data=request.data)
    
    if login_serializer.is_valid():
        username = login_serializer.validated_data["username"]
        password = login_serializer.validated_data["password"]
        
        user = User.objects.filter(username=username).first()
                
        if user is None:
            return Response(
                {"error" : "User does not exists."},
                status=401
            )
            
        if not user.check_password(password):
            return Response(
                {"error" : "Invalid Password."},
                status=401
            )
        
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response(
            {"message" : "Logging in",
             "username" : user.username,
             "token" : token.key}
        )

    return Response(login_serializer.errors, status=400)