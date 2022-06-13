# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# from accounts import models
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Registration successful!!!'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }  
        else:
            data = serializer.errors
        return Response(data)
    

class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# @api_view(['POST',])
# def registration_view(request):
    
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
            
#             data['response'] = 'Registration successful!!!'
#             data['username'] = account.username
#             data['email'] = account.email
            
#             refresh = RefreshToken.for_user(account)
#             data['token'] = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
            
#         else:
#             data = serializer.errors
#         return Response(data)
    

# @api_view(['POST',])
# def logout_apiview(request):
#     if request.method == 'POST':
#         request.user.auth_token.delete()
#     return Response(status=status.HTTP_200_OK)
