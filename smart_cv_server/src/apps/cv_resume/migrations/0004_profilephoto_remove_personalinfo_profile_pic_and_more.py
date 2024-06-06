# Generated by Django 4.2.11 on 2024-06-03 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv_resume', '0003_alter_personalinfo_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='profile_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv_resume.profilephoto'),
        ),
    ]
