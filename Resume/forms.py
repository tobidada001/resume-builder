from .models import User
from django import forms

class UserSignUpForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = '__all__'


class UserSignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
