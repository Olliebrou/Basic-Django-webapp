from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']