# Generated by Django 4.1 on 2023-10-11 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0002_additionalprofile_workexperience_skill_reference_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='duration',
        ),
        migrations.AddField(
            model_name='additionalprofile',
            name='uniqueid',
            field=models.UUIDField(default=uuid.UUID('21813a47-ca0d-4cd6-b6ae-5b487ee8071d'), unique=True),
        ),
        migrations.AlterField(
            model_name='additionalprofile',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='additionalprofile',
            name='profile_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='additionalprofile',
            name='profile_summary',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='additionalprofile',
            name='residential_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.additionalprofile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='your_role',
            field=models.CharField(max_length=100),
        ),
    ]