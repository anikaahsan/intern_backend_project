from django.urls import path
from auth.rest.views.password import ForgotPasswordView, ResetPasswordView,TokenView

urlpatterns = [
    path("/forgot-password", ForgotPasswordView.as_view(), name="forgot-password"),
      path("/verify-token", TokenView.as_view(), name="verify-token"),
    path("/reset-password", ResetPasswordView.as_view(), name="reset-password"),
]