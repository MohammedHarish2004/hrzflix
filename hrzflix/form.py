from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':''}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':''}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':''}))

    class Meta:
        model =User
        fields = ['username','email','password1','password2']