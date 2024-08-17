from django.shortcuts import render

from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
import traceback
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework.authentication import BasicAuthentication
from .models import User
from rest_framework.views import APIView
from .user_tokens import get_user_tokens
from rest_framework import authentication

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        print('start user RegisterSerializer')
        try:
            user_role = request.data
            if user_role == 'AM':
                return Response({'message': 'You do not have permissions to create user',}, status=status.HTTP_409_CONFLICT)
            data = request.data
            serializer = self.get_serializer(data=data)
            if not serializer.is_valid():
                return Response({'message': 'user with this email already exists',}, status=status.HTTP_409_CONFLICT)
            user = serializer.save()
            
            return Response({'status': 'User Register Sucessfully'}, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex, 'user issue RegisterSerializer')
            print(traceback.print_exc())
            return Response(status=status.HTTP_400_BAD_REQUEST)




class LoginAPI(generics.GenericAPIView):

  serializer_class = LoginSerializer

  def post(self, request):
    try:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        user = serializer.validated_data
        print(f'user data :{user}')
        refresh, access = get_user_tokens(user)  
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,"refresh": refresh,"access":access}, status=status.HTTP_200_OK)


    except Exception as ex:
        print(ex, 'user issue login')
        print(traceback.print_exc())
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
       