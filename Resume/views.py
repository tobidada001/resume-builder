from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import FormView
from .models import UserForm
from .forms import UserSignInForm, UserSignUpForm
# Create your views here.
def index(request):
    return render(request, 'srt-resume.html')

class UserSignUpView(FormView):
    model = UserForm
    form_class = UserSignUpForm
    template_name = "index.html"

class UserSignInView(FormView):
    model = UserForm
    form_class = UserSignInForm
    template_name = "index.html"
