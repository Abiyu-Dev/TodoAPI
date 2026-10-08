from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]



class MeView(APIView):
    def get(self, user):
        user = request.user

        return Response(
            {
                'id':user.id,
                'email':user.email,
                'username':user.username
            },
            status=status.HTTP_200_OK,
        )



class CustomTokenObtainPairView(TokenObtainPairView):
    """Login endpoint with a customized payload. See serializer for details."""
    serializer_class = CustomTokenObtainPairSerializer