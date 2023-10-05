from .models import UserForm
from django import forms

class UserSignUpForm(forms.ModelForm):
   
    class Meta:
        model = UserForm
        fields = '__all__'


class UserSignInForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = '__all__'
