from django.db import models
from django.utils.translation import gettext as _ 
from  django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User as U
import uuid

class User(AbstractUser):
    email = models.EmailField(_("Email Address"), max_length=250, unique= True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return str(self.first_name) + ' <<>> ' + str(self.last_name)
    

class AdditionalProfile(models.Model):
    residential_address = models.CharField(max_length=200)
    phone = models.CharField( max_length=50)
    profile_summary = models.TextField( max_length=500)
    profile_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uniqueid = models.UUIDField(unique= True, blank=True, null=True)

    def save(self, *args, **kwargs):
       self.uniqueid = uuid.uuid4()
       super(AdditionalProfile, self).save(*args, **kwargs) # Call the real save() method


class WorkExperience(models.Model):
    job_title = models.CharField( max_length=80)
    company = models.CharField( max_length=80)
    achievement = models.TextField()
    started_from = models.DateField( auto_now=False, auto_now_add=False)
    stopped_at = models.DateField( auto_now=False, auto_now_add=False)
    work_experience_owner = models.ForeignKey(AdditionalProfile, on_delete=models.CASCADE)
    


class Education(models.Model):
    degree = models.CharField( max_length=50)
    institution = models.CharField( max_length=100)
    started_from = models.DateField( auto_now=False, auto_now_add=False)
    stopped_at = models.DateField( auto_now=False, auto_now_add=False)
    education_owner = models.ForeignKey(AdditionalProfile, on_delete=models.CASCADE)



class Project(models.Model):
    title = models.CharField(max_length=100)
    your_role = models.CharField( max_length=100)
    description = models.TextField()
    proj_duration = models.CharField( max_length=50)
    project_owner = models.ForeignKey(AdditionalProfile, on_delete=models.CASCADE)

    
class Reference(models.Model):
    name = models.CharField(_(""), max_length=100)
    contact_info = models.CharField(_(""), max_length=250)
    reference_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)


class Language(models.Model):
    language = models.CharField(_(""), max_length=80)
    fluency_level = models.CharField(_(""), max_length=50)
    language_owner = models.ForeignKey(AdditionalProfile, verbose_name=_(""), on_delete=models.CASCADE)


class Skill(models.Model):
    skill = models.CharField( max_length=50)
    skill_owner = models.ForeignKey(AdditionalProfile, on_delete=models.CASCADE)