

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from .serializer import RegisterSerializer


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
    


    