from allauth.account.signals import email_confirmed
from django.dispatch import receiver

@receiver(email_confirmed)
def email_confirmed_handler(request, email_address, **kwargs):
    user = email_address.user
    user.userprofile.email_verified = True
    user.userprofile.save()