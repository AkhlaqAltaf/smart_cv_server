from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from src.api.cv_resume.serializers import  CVResumeSerializer
from src.apps.cv_resume.models import CVResume


class ResumeCreateView(viewsets.ModelViewSet):
    queryset = CVResume.objects.all()
    serializer_class =CVResumeSerializer
    permission_classes = [AllowAny]
