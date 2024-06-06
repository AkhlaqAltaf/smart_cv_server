# Generated by Django 4.2.11 on 2024-06-04 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv_resume', '0007_personalinfo_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='profile_photo',
        ),
        migrations.AddField(
            model_name='cvresume',
            name='prifile_picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv_resume.profilephoto'),
        ),
    ]
