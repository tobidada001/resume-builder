from django.db import models
from django.utils.translation import gettext as _ 
from  django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(_("Email Address"), max_length=250, unique= True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    def __str__(self):
        return str(self.first_name) + ' <<>> ' + str(self.last_name)
    

class AdditionalProfile(models.Model):
    residential_address = models.CharField(_(""), max_length=200)
    phone = models.CharField(_(""), max_length=50)
    profile_summary = models.TextField(_(""), max_length=500)
    profile_owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)


class WorkExperience(models.Model):
    job_title = models.CharField(_(""), max_length=80)
    company = models.CharField(_(""), max_length=80)
    achievement = models.TextField(_(""))
    started_from = models.DateField(_(""), auto_now=False, auto_now_add=False)
    stopped_at = models.DateField(_(""), auto_now=False, auto_now_add=False)
    work_experience_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)
    


class Education(models.Model):
    degree = models.CharField(_(""), max_length=50)
    institution = models.CharField(_(""), max_length=100)
    started_from = models.DateField(_(""), auto_now=False, auto_now_add=False)
    stopped_at = models.DateField(_(""), auto_now=False, auto_now_add=False)
    education_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)



class Project(models.Model):
    title = models.CharField(_(""), max_length=100)
    your_role = models.CharField(_(""), max_length=100)
    description = models.TextField(_(""))
    proj_duration = models.CharField(_(""), max_length=50)
    duration = models.DurationField(_(""))
    project_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)

    
class Reference(models.Model):
    name = models.CharField(_(""), max_length=100)
    contact_info = models.CharField(_(""), max_length=250)
    reference_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)


class Language(models.Model):
    language = models.CharField(_(""), max_length=80)
    fluency_level = models.CharField(_(""), max_length=50)
    language_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)


class Skill(models.Model):
    skill = models.CharField(_(""), max_length=50)
    skill_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)