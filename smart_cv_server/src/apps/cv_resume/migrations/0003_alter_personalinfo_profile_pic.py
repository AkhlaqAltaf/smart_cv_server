# Generated by Django 5.0.3 on 2024-04-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_resume', '0002_personalinfo_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]