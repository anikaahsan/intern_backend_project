from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator

User = get_user_model()



def verify_token(user,token):
        print(f"[DEBUG] Verifying token for user={user.email}")
        print(f"[DEBUG] Token valid? {PasswordResetTokenGenerator().check_token(user, token)}")
        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
                raise serializers.ValidationError("Invalid or expired token or already used.")


# check whether user exist or not with email
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value

#verify the token
class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True)    

    def validate(self, data):
       
        email=self.context.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user")
        
        # token_generator = PasswordResetTokenGenerator()
        # if not token_generator.check_token(user, data["token"]):
        #     raise serializers.ValidationError("Invalid or expired token.")

        verify_token(user,data['token'])
        
        return data

        


class ResetPasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [ 'new_password','confirm_password']
    
   
    def validate(self, data):
       
        try:
            self.user = User.objects.get(email=self.context.get('email'))
          
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user ")
        
        verify_token(self.user,self.context.get('token'))
        
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def save(self, **kwargs):

        self.user.set_password(self.validated_data["new_password"])
        self.user.save()
        return self.user    
