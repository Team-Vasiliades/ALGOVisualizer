from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_photo', 'password1', 'password2']
 

