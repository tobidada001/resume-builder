from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import FormView
from .models import User

from .forms import UserSignInForm, UserSignUpForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

class UserSignUpView(FormView):
    model = User
    form_class = UserSignUpForm
    template_name = "index.html"

class UserSignInView(FormView):
    model = User
    form_class = UserSignInForm
    template_name = "index.html"

def create_new(request):
    if request.method== 'POST':
        print(request.POST)
    return render(request, 'add_details.html')

