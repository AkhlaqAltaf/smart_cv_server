from django.contrib.auth.models import User
from django.db import models


# PERSONAL INFORMATION
class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True ,null=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language, through="PersonalLanguage")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'personal_info'
        ordering = ('-created_at',)

    def __str__(self):
        return self.full_name


class PersonalLanguage(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.personal_info.full_name


# WORK EXPERIENCE


class WorkExperience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.CharField(max_length=50)

    def __str__(self):
        return self.responsibilities


# SKILLS

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# EDUCATION

class Education(models.Model):
    name = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    graduation_year = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# CERTIFICATION AND AWARD

class Certification(models.Model):
    name = models.CharField(max_length=50)
    issuer_name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name


# CVRESUME


class CVResume(models.Model):

    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    workExperience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, through='CVSkill')

    def __str__(self):
        return self.personal_info.full_name


class CVSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    cv_resume = models.ForeignKey(CVResume, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill.name
