from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user):
    subject = 'Thank you for Signing Up with ProHR!'
    message = f'Hi, { user.username } ! \n Thank you for signing up on ProHR! \n Your account has been successfully created, \n and you’re now ready to explore exciting opportunities.'
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # From email
        [user.email],  # Recipient email
        fail_silently=False,  # To raise exceptions if any error occurs
    )