import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from weasyprint import HTML

from src.api.cv_resume.ai.generate import CVGenAI
from src.api.cv_resume.serializers import CVResumeSerializer, DownloadCVResumeSerializer
from src.apps.cv_resume.models import CVResume


class ResumeView(viewsets.ModelViewSet):
    queryset = CVResume.objects.all()
    serializer_class = CVResumeSerializer
    permission_classes = [AllowAny]


class DownloadCvResumeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = DownloadCVResumeSerializer

    def get(self, request, *args, **kwargs):
        _id = kwargs.get('cv_resume_id')
        template_type = kwargs.get('template_type')
        gen_ai = CVGenAI()
        cv_resume = get_object_or_404(CVResume, pk=_id)
        if cv_resume.prifile_picture:
            profile_ = cv_resume.prifile_picture.profile_pic.url
        else:
            profile_ = None
        body = gen_ai.generate_cv_body(cv_resume)
        cv_resume.body = body


        profile_pic_url = request.build_absolute_uri(profile_)
        template = get_template(f'cv_resumes/{template_type}.html')
        html = template.render({'cv_resume': cv_resume, 'profile_pic_url': profile_pic_url})

        pdf_file = HTML(string=html).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cv_resume.personal_info.full_name}.pdf"'
        return response


class CVResumeCreateView(APIView):
    permission_classes = [AllowAny]

    parser_classes = (MultiPartParser, FormParser)


    def post(self, request, *args, **kwargs):

        data = request.data.dict()
        print(data)

        personal_info = json.loads(data.get('personal_info'))
        education = json.loads(data.get('education'))
        work_experience = json.loads(data.get('work_experience'))
        certification = json.loads(data.get('certification'))
        skills = json.loads(data.get('skills'))
        profile_picture = request.FILES.get('profile_picture')

        data['personal_info'] = personal_info
        data['education'] = education
        data['work_experience'] = work_experience
        data['certification'] = certification
        data['skills'] = skills
        data['profile_picture'] = {'profile_pic': profile_picture}

        serializer = CVResumeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetCVResumesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        serializer = CVResumeSerializer()
        cv_resumes = serializer.get_cv_resumes(id)
        return Response(cv_resumes)