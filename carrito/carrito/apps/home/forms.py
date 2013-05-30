from django import forms
#importamos la libreria de formulario de django
from django.contrib.auth.models import User

class ContactForm(forms.Form):
	Email  = forms.EmailField(widget=forms.TextInput())
	Titulo = forms.CharField(widget=forms.TextInput())
	Texto  = forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))