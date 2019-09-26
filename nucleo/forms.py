from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"type": "text", "name": "username", "autocomplete": "username", "id": "username",
               "placeholder": "Ingrese correo electronico", "class": "form-control"}), required=True)
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "password", "name": "password", "id": "password", "placeholder": "Ingrese contraseña",
                   "class": "form-control"}), required=True)
