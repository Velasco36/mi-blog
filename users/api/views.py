

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from users.models import User

from .serializer import *


class RegisterView(APIView):
    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    name = 'register'
    
    
    
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('test')
            return Response(serializer.data)
        
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        #request.
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    