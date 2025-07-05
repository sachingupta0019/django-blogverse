# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),max_length=10, required=False)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select'}), choices=GENDER_CHOICES, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False, max_length=128)
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}), required=False)

    class Meta:
        model = User 
        fields = ['username', 'email', 'first_name','last_name','password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={"class":"form-control","reuired":True}),
            'first_name': forms.TextInput(attrs={"class":"form-control"}),
            'last_name': forms.TextInput(attrs={"class":"form-control"}),
        }

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class":"form-control","autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class":"form-control","autocomplete": "current-password"}),
    )