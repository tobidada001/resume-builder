# Generated by Django 4.1 on 2023-10-12 00:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0003_remove_project_duration_additionalprofile_uniqueid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalprofile',
            name='uniqueid',
            field=models.UUIDField(default=uuid.UUID('8bb8f9cd-5897-48c4-902f-00fa36c20bce'), unique=True),
        ),
    ]
