# Generated by Django 4.2.11 on 2024-05-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_letter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='experience',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='job_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]