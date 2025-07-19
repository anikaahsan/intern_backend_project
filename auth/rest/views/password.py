
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from auth.rest.serializers.password import ForgotPasswordSerializer, ResetPasswordSerializer,TokenSerializer

User = get_user_model()





class ForgotPasswordView(CreateAPIView):
    serializer_class = ForgotPasswordSerializer
    
    @swagger_auto_schema(request_body=ForgotPasswordSerializer)
    def create(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
           
        user = User.objects.get(email=serializer.validated_data["email"])
        token = PasswordResetTokenGenerator().make_token(user)
        email= user.email
        reset_url = f"http://127.0.0.1:8000/api/v1/auth/password/verify-token?email={email}"

        send_mail(
            subject="Reset Your Password",
            message=f"Use this link to reset your password: {reset_url} \n Enter the one-time token for verification.\nYour one-time token is: { token } \n Your token  will be expired in 5 minutes" ,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
        return Response({"detail": "Password reset email sent."}, status=status.HTTP_200_OK)

        

#verify token
class TokenView(CreateAPIView):
    serializer_class = TokenSerializer

    @swagger_auto_schema(request_body=TokenSerializer)
    def create(self, request, *args, **kwargs):
        email=request.query_params.get('email')
        
        serializer=self.get_serializer(data=request.data,context={'email':email})
        serializer.is_valid(raise_exception=True)
        token=serializer.validated_data['token']
        return Response(
            {
                "detail": "token matched.click on the below link to set new password",
                 "redirect_to": f"http://127.0.0.1:8000/api/v1/auth/password/reset-password?email={email}&t={token}"
            },
            
        )


          
            

class ResetPasswordView(CreateAPIView):
    serializer_class = ResetPasswordSerializer

    @swagger_auto_schema(request_body=ResetPasswordSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'email':request.query_params.get('email'),'token':request.query_params.get('t')})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password has been reset."}, status=status.HTTP_200_OK)
      