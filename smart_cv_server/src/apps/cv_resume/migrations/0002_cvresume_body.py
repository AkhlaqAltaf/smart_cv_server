# Generated by Django 4.2.11 on 2024-06-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvresume',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
