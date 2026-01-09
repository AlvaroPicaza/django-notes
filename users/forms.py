from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
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


###### Login usuario ######

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(label="Nombre de usuario")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"Usuario"
        })

        self.fields["password"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"Contraseña"
        })
        self.helper = FormHelper()
        self.helper.form_tag = False 


##### Actualizar datos del usuario ######

class UserUpdateForm(forms.ModelForm):
    
    username = forms.CharField(label="Nombre de usuario",
                               help_text="150 caracteres o menos. Letras, números y símbolos @/./+/-/_ ",
                               error_messages={'unique': ("Ya existe un usuario con ese nombre.")},
                               widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(label="Correo electrónico"                        
    )

    class Meta:
        model = User
        fields = ['username','email']




###### Actualizar perfil del usuario #######

class CustomImageWidget(forms.ClearableFileInput):
    initial_text = "Foto actual"
    template_name = 'django/forms/widgets/clearable_file_input.html'

class ProfileUpdateForm(forms.ModelForm):

    image = forms.ImageField(label="Foto de perfil")

    class Meta:
        model = Profile
        fields = ['image']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Accedemos al widget para cambiar los textos específicos
        self.fields['image'].widget.initial_text = 'Foto actual'