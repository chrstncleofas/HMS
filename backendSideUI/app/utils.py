# utils.py
from django.core.mail import EmailMessage

def process_user_update(user):
    send_welcome_email(user)
    perform_additional_operations(user)

def send_welcome_email(user):
    subject = 'Welcome to Our Platform'
    message = f'Hello {user.username},\n\nThank you for joining our platform!'
    email = EmailMessage(subject, message, to=[user.email])
    email.send()

def perform_additional_operations(user):
    # Ito ay halimbawa lamang, maaaring ilagay dito ang karagdagang logic o operasyon na nais gawin.
    user.is_active = True  # Itakda ang user na active matapos ma-update
    user.save()
    # Maaaring idagdag ang iba pang mga operasyon tulad ng pag-update ng iba pang modelo o pagproseso ng iba't ibang data.
