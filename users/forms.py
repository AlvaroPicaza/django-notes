from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import Profile
from crispy_forms.helper import FormHelper

from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class UserRegisterForm(UserCreationForm):
    

    username = forms.CharField(label="Nombre de usuario",
                               help_text= ('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                               validators=[username_validator],
                                error_messages={'unique': ("A user with that username already exists.")},
                                widget=forms.TextInput(attrs={'class': 'form-control'})        
            )
    email = forms.EmailField(help_text="Requerido. Se necesita un mail válido")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label="Repita su contraseña",widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=password_validation.password_validators_help_text_html())

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False 


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(help_text="A valid email address, please.")

    class Meta:
        model = User
        fields = ['username','email']

"""class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']"""