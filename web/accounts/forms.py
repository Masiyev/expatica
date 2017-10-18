from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
    username = forms.CharField(label="Username", max_length=30,
            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'required': 'true'}))
    password = forms.CharField(label="Password", max_length=30,
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'required': 'true'}))

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    username = forms.CharField(label="", required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': 'true'}))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': 'true'}))
    first_name = forms.CharField(label="", required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'required': 'true'}))
    last_name = forms.CharField(label="", required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'required': 'true'}))
    password1 = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'true'}))
    password2 = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat your password', 'required': 'true'}))

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
