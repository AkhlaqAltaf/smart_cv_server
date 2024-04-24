import os.path
from io import BytesIO

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from requests import Response
from rest_framework import viewsets, response
from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from xhtml2pdf import pisa

from smart_cv_server.settings import BASE_DIR
from src.api.cv_resume.serializers import CVResumeSerializer, DownloadCVResumeSerializer
from src.apps.cv_resume.models import CVResume, PersonalInfo, Education, WorkExperience, Certification, \
    PersonalLanguage, Language, Skill, CVSkill


class ResumeView(viewsets.ModelViewSet):
    queryset = CVResume.objects.all()
    serializer_class = CVResumeSerializer
    permission_classes = [AllowAny]


class DownloadCvResumeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = DownloadCVResumeSerializer
    def get(self, request, *args, **kwargs):
        _id = kwargs.get('cv_resume_id')
        cv_resume = get_object_or_404(CVResume, pk=_id)

        print("CV RESUME ", cv_resume.personal_info.profile_pic)
        template = get_template('templates/practice_template.html')
        style_file = os.path.join(BASE_DIR, 'static', 'css', 'templates', 'template1.css')
        html = template.render({'cv_resume': cv_resume, 'style_file': style_file})

        buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=buffer)
        if pisa_status.err:
            return HttpResponse('PDF generation error!', status=500)

        pdf_data = buffer.getvalue()
        buffer.close()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cv_resume.personal_info.full_name}.pdf"'
        response.write(pdf_data)

        return response


class CreateCvResume(APIView):
    permission_classes = [AllowAny]
    serializer_class =CVResumeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cv_resume =serializer.create(request.data)
            response = HttpResponse(content_type='application/pdf')
            response['id']=cv_resume
            return response

        else:
            return HttpResponse("Data Not Valid")

