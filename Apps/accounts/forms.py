"""User forms. bien"""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.Form):
    """Sign up form."""
    username = forms.CharField(
        min_length=4, 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese nombre de usuario.', 'style' : 'border-color:#21B64A;'}),
        label = 'Nombre de Usuario: *',
    )

    first_name = forms.CharField(
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese nombre.', 'style' : 'border-color:#21B64A;'}),
        label = 'Nombre(s):',
    )
    last_name = forms.CharField(
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Apellido.', 'style' : 'border-color:#21B64A;'}),
        label = 'Apellidos:',
    )

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'ejemplo@ejemplo.com', 'style' : 'border-color:#21B64A;'}),
        label = 'Correo electronico: *',
    )

    # user_permissions = forms.CharField(
    #     widget=forms.SelectMultiple(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}),
    #     label = 'Permisos: *',
    # )

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese contraseña.', 'style' : 'border-color:#21B64A;'}),
        label = 'Contraseña:',
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirme su contraseña', 'style' : 'border-color:#21B64A;'}),
        label = 'Confirmacion de Contraseña:'
    )

    #Valida que el nombre de usuario no exista 
    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El nombre de usuario ya está en uso.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()