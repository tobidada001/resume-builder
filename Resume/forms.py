from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms
class UserSignUpForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields.pop('password')
        
        for field in self.fields.values(): 
            field.widget.attrs['class'] = "flex-1 pl-4"
        

class AuthLoginForm(AuthenticationForm):
    
    email = forms.CharField(widget= forms.TextInput(attrs={"class": "flex-1"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs= {"class": 'flex-1'}))

    
    def __init__(self, *args, **kwargs):
        super(AuthLoginForm, self).__init__(*args, **kwargs)
        self.fields.pop('username')
    

class UserSignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
