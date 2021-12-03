from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms

class SignUpFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        labels = {'email':'Email'}