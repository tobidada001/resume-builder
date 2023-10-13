
import django.contrib.auth.models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
import pdfkit


# Create your views here.
def index(request):
    return render(request, 'index.html')


def choose_template(request, profile):
    profile = get_object_or_404(AdditionalProfile, uniqueid = profile)
    templates= ResumeTemplates.objects.all()
    return render(request, 'choose-template.html', {'templates': templates, 'profile': profile})



def assigntemplate(request, profile, tid):
    profile = get_object_or_404(AdditionalProfile, uniqueid = profile)
    if tid:
        profile.templateid = tid
        profile.save()
        return redirect(reverse('completed', kwargs={'profile': profile.uniqueid}))
    else:
        return redirect('/')



def signupview(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next')) if request.GET.get('next') else redirect('/')
    
    userform = UserSignUpForm()

    if request.method == 'POST':
        theform  = UserSignUpForm(request.POST)
        if theform.is_valid():
            theform.save()
            auth = authenticate(email = theform.cleaned_data['email'], password = theform.cleaned_data['password1'])
            print('User: ', auth)
            # print('User saved.')
            login(request, auth)

            return redirect('all_resumes')
        else:
            print('Incorrect details')

            return redirect('signup')
    return render(request, 'signup.html', {'form': userform})

def loginview(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next')) if request.GET.get('next') else redirect('/')
    
    if request.method == 'POST':
        auth = authenticate(username = request.POST['email'], password = request.POST['password'])
        if auth:
            login(request, auth)
            return redirect(request.GET.get('next')) if request.GET.get('next') else redirect('/')
        else:
            return redirect('login')
        
    return render(request, 'signin.html')

@login_required(login_url='/login/')
def all(request):
    resumes = request.user
    return render(request, 'allresumes.html', {'user': resumes})

def create_new(request):
    if request.method== 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        res_address = request.POST['res_address']
        phone = request.POST['phonenumber']
        summary = request.POST['aboutyou']
        profile_owner = request.user
        

        if not request.user.is_authenticated:
            newuser = User.objects.create_user(email = email, username = email, password = lname, first_name = fname, last_name = lname)
            auth = authenticate(username = newuser.email, password = newuser.password)

            if auth:
                login(request, auth)

        AdditionalProfile.objects.create(residential_address = res_address, phone = phone, profile_summary = summary, profile_owner = profile_owner)
        profile = AdditionalProfile.objects.filter(profile_owner = request.user).first()

       
        for i in range(1, 200):
            jobtitle = request.POST.get(f'job_title{i}')
            if jobtitle:
                jobcompany = request.POST[f'job_organization{i}']
                achievement = request.POST[f'job_achievement{i}']
                job_started_from = request.POST['job_from'+str(i)]
                job_stopped_at = request.POST[f'job_to{i}']
               
                WorkExperience.objects.create(job_title = jobtitle, company = jobcompany, achievement =achievement, started_from = job_started_from, 
                                              stopped_at = job_stopped_at, work_experience_owner = profile)
        

            degree = request.POST.get(f'degree{i}')
            if degree:
                institution = request.POST[f'institute_name{i}']
                deg_start = request.POST[f'institute_from{i}']
                deg_end= request.POST[f'institute_to{i}']

                Education.objects.create(degree = degree, institution = institution, started_from = deg_start, stopped_at = deg_end, education_owner = profile)

        
            proj_title = request.POST.get(f'proj_title{i}')
            if proj_title:
                your_role = request.POST[f'proj_role{i}']
                proj_desc = request.POST[f'proj_desc{i}']
                proj_dur = request.POST[f'proj_duration{i}']

                Project.objects.create(title = proj_title , your_role = your_role, description = proj_desc, proj_duration = proj_dur, project_owner = profile)
        

            ref_name = request.POST.get(f'ref_name{i}')

            if ref_name:
                ref_info = request.POST[f'ref_contact{i}']
                Reference.objects.create(name = ref_name,  contact_info = ref_info,   reference_owner = profile)


            lang = request.POST.get(f'language{i}')

            if lang:
                fluency = request.POST[f'language_level{i}']
                Language.objects.create(language = lang , fluency_level = fluency, language_owner = profile)

        
            skill = request.POST.get(f'skill{i}')
            if skill:
                Skill.objects.create(skill = skill, skill_owner = profile)

            
            if not jobtitle and not degree and not proj_title and not ref_name and not skill and not lang and not degree:
                break

        choose_template_url = reverse('choose_template', kwargs={'profile': profile.uniqueid})
        return redirect(choose_template_url)
    

    return render(request, 'add_details.html')

def completed(request, profile):
    profile = get_object_or_404(AdditionalProfile, uniqueid = profile) 
    return render(request, 'completed.html', {'profile': profile})

def seeprofile(request, profile):
    profile = get_object_or_404(AdditionalProfile, uniqueid = profile)
    if profile.templateid > 0:
        print('This is working')
        return render(request, f'resume{profile.templateid}.html', {'profile': profile})
    else:
        print('This s not working')
        return render(request, f'resume1.html', {'profile': profile})

def downloadpdf(request, profile):

    profile = get_object_or_404(AdditionalProfile, uniqueid = profile)

    temp = render_to_string('resume6.html', context={'profile' : profile}, request= request)
    options = {"enable-local-file-access": "",
               'Page-Size': "A4", 
               'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(temp, False, options = options)

    resp =  HttpResponse(pdf, content_type = "application/pdf")
    resp['Content-Disposition'] = f"attachment;filename={profile.profile_owner.first_name}.pdf"

    return resp
