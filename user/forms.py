from allauth.account.forms import LoginForm, SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    profile_picture = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(label='Email Address')
    is_premium = forms.BooleanField(label='Premium Account', required=False, default=False)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()

        profile = user.userprofile
        profile.is_premium = self.cleaned_data['is_premium']
        if self.cleaned_data['profile_picture']:
            profile.profile_picture = self.cleaned_data['profile_picture']
        profile.save()

        return user