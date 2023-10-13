from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.AdditionalProfile)
admin.site.register(models.Education)
admin.site.register(models.Language)
admin.site.register(models.Project)
admin.site.register(models.Reference)
admin.site.register(models.Skill)
admin.site.register(models.WorkExperience)
admin.site.register(models.ResumeTemplates)