from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import usercontact, newProduct
from django.contrib.auth.models import User

class contactForm(forms.ModelForm):
    class Meta : 
        model = usercontact
        fields = '__all__'


class addProduct(forms.ModelForm):
    class Meta : 
        model = newProduct
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    class Meta : 
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
