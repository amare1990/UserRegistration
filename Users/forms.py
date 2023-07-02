from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    phone_number = forms.CharField(max_length=20)
    # image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name', 'email', 'phone_number', 'password1', 'password2']


class CustomPasswordResetForm(PasswordResetForm):
    # Add any additional fields or customizations here
    email_address = forms.EmailField(label='Email Address')
