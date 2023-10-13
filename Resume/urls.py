from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup/', views.signupview, name = 'signup'),
    path('login/', views.loginview, name = 'login'),
    path('create-new/', views.create_new, name='create_new'),
    path('view-resume/<slug:profile>/', views.seeprofile, name= 'resumepath'),
    path('download/<slug:profile>/', views.downloadpdf, name='download'),
    path('completed/<slug:profile>/', views.completed, name= 'completed'),
    path('all/', views.all, name='all_resumes')
]
