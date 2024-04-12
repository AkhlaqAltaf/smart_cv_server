from rest_framework import serializers
from src.apps.cv_resume.models import PersonalInfo, WorkExperience, Skill, Education, Certification, CVResume, \
    PersonalLanguage, CVSkill, Language
from django.contrib.auth.models import User


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class PersonalInfoSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)

    class Meta:
        model = PersonalInfo
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'


class CVResumeSerializer(serializers.ModelSerializer):
    personal_info = PersonalInfoSerializer()
    education = EducationSerializer()
    workExperience = WorkExperienceSerializer()
    certification = CertificationSerializer()
    skills = SkillSerializer(many=True)

    class Meta:
        model = CVResume
        fields = '__all__'

    def create(self, validated_data):
        # GET DATA

        personal_info_data = validated_data.pop('personal_info')
        education_data = validated_data.pop('education')
        work_experience_data = validated_data.pop('workExperience')
        certification_data = validated_data.pop('certification')
        skills_data = validated_data.pop('skills')
        languages_data = personal_info_data.pop('languages')

        # POST DATA

        personal_info = PersonalInfo.objects.create(**personal_info_data)
        education = Education.objects.create(**education_data)
        work_experience = WorkExperience.objects.create(**work_experience_data)
        certification = Certification.objects.create(**certification_data)

        for language_data in languages_data:
            language, create = Language.objects.get_or_create(**language_data)
            PersonalLanguage.objects.create(personal_info=personal_info, language=language)
        cv_resume = CVResume.objects.create(
            personal_info=personal_info,
            education=education,
            workExperience=work_experience,
            certification=certification
        )

        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(**skill_data)
            CVSkill.objects.create(cv_resume=cv_resume, skill=skill)

        return cv_resume

    def update(self, instance, validated_data):
        personal_info_data = validated_data.pop('personal_info')
        education_data = validated_data.pop('education')
        work_experience_data = validated_data.pop('workExperience')
        certification_data = validated_data.pop('certification')
        skills_data = validated_data.pop('skills')
        languages_data = personal_info_data.pop('languages')

        personal_info_serializer = self.fields['personal_info']
        education_serializer = self.fields['education']
        work_experience_serializer = self.fields['workExperience']
        certification_serializer = self.fields['certification']
        skills_serializer = self.fields['skills']

        personal_info_instance = personal_info_serializer.update(instance.personal_info, personal_info_data)
        education_instance = education_serializer.update(instance.education, education_data)
        work_experience_instance = work_experience_serializer.update(instance.workExperience, work_experience_data)
        certification_instance = certification_serializer.update(instance.certification, certification_data)

        # Update many-to-many field 'skills'
        instance.skills.clear()
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(**skill_data)
            instance.skills.add(skill)

        # Update many-to-many field 'languages' of personal_info
        instance.personal_info.languages.clear()
        for language_data in languages_data:
            language, _ = Language.objects.get_or_create(**language_data)
            PersonalLanguage.objects.create(personal_info=personal_info_instance, language=language)

        instance.save()

        return instance



