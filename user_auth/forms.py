from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ('phone', 'username', 'last_name', 'email', 'password1', 'password2')

