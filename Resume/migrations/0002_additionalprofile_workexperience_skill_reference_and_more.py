# Generated by Django 4.1 on 2023-10-08 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residential_address', models.CharField(max_length=200, verbose_name='')),
                ('phone', models.CharField(max_length=50, verbose_name='')),
                ('profile_summary', models.TextField(max_length=500, verbose_name='')),
                ('profile_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=80, verbose_name='')),
                ('company', models.CharField(max_length=80, verbose_name='')),
                ('achievement', models.TextField(verbose_name='')),
                ('started_from', models.DateField(verbose_name='')),
                ('stopped_at', models.DateField(verbose_name='')),
                ('work_experience_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.additionalprofile', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, verbose_name='')),
                ('skill_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.additionalprofile', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('contact_info', models.CharField(max_length=250, verbose_name='')),
                ('reference_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.additionalprofile', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='')),
                ('your_role', models.CharField(max_length=100, verbose_name='')),
                ('description', models.TextField(verbose_name='')),
                ('proj_duration', models.CharField(max_length=50, verbose_name='')),
                ('duration', models.DurationField(verbose_name='')),
                ('project_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.additionalprofile', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=80, verbose_name='')),
                ('fluency_level', models.CharField(max_length=50, verbose_name='')),
                ('language_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.additionalprofile', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50, verbose_name='')),
                ('institution', models.CharField(max_length=100, verbose_name='')),
                ('started_from', models.DateField(verbose_name='')),
                ('stopped_at', models.DateField(verbose_name='')),
                ('education_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.additionalprofile', verbose_name='')),
            ],
        ),
    ]
