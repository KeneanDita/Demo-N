from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter a Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Cpnfirm Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))