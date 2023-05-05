from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name', 'email', 'phone_number', 'password1', 'password2']
