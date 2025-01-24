from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class CustomUserCreationForm(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'mt-2 bg-transparent border-b-2 border-gray-500 focus:outline-none focus:border-blue-500'
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'mt-2 bg-transparent border-b-2 border-gray-500 focus:outline-none focus:border-blue-500'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'mt-2 bg-transparent border-b-2 border-gray-500 focus:outline-none focus:border-blue-500'
    }))

    student_id = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Student ID',
        'class': 'mt-2 bg-transparent border-b-2 border-gray-500 focus:outline-none focus:border-blue-500'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'mt-2 bg-transparent border-b-2 border-gray-500 focus:outline-none focus:border-blue-500'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'mt-2 bg-transparent border-b-2 border-gray-500 focus:outline-none focus:border-blue-500'
    }))

    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'email', 'student_id', 'password1', 'password2']
    