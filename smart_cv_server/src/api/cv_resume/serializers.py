from rest_framework import serializers
from src.apps.cv_resume.models import CVResume, PersonalInfo, Education, WorkExperience, Certification, Skill


class CVResumeSerializer(serializers.ModelSerializer):
    personal_info = serializers.PrimaryKeyRelatedField(queryset=PersonalInfo.objects.all())
    education = serializers.PrimaryKeyRelatedField(queryset=Education.objects.all())
    work_experience = serializers.PrimaryKeyRelatedField(queryset=WorkExperience.objects.all())
    certification = serializers.PrimaryKeyRelatedField(queryset=Certification.objects.all())
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)


    class Meta:
        model = CVResume
        fields = '__all__'

