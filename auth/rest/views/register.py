from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from auth.rest.serializers.register import UserRegisterSerializer
from auth.rest.services import send_welcome_email

class UserRegisterView(CreateAPIView):
    """User registration view"""

    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email(user)