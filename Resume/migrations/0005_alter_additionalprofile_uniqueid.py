# Generated by Django 4.1 on 2023-10-12 00:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0004_alter_additionalprofile_uniqueid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalprofile',
            name='uniqueid',
            field=models.UUIDField(default=uuid.UUID('6728c949-f125-4f2c-b369-818f06de6f49'), unique=True),
        ),
    ]
