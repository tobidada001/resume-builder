from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('create', views.UserSignUpView.as_view()),
    path('login', views.UserSignInView.as_view())
]