from io import BytesIO
from io import BytesIO

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.utils import json
from rest_framework.views import APIView
from xhtml2pdf import pisa

from src.api.cover_letter.ai.generate import CoverLetterGenAI
from src.api.cover_letter.serializers import CoverLetterSerializer
from src.apps.cover_letter.models import CoverLetter


class CoverLetterView(viewsets.ModelViewSet):
    queryset = CoverLetter.objects.all()
    serializer_class = CoverLetterSerializer
    permission_classes = [AllowAny]


class DownloadCoverLetter(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        _id = kwargs.get('cover_letter_id')
        type = kwargs.get('cover_letter_type')
        cover_letter = get_object_or_404(CoverLetter, pk=_id)

        ai = CoverLetterGenAI()
        body = ai.generate_cover_letter_body(cover_letter=cover_letter)
        print(body)
        cover_letter.body = body
        template = get_template(f'cover_letters/{type}.html')
        html = template.render({'cover_letter': cover_letter})

        buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=buffer)
        if pisa_status.err:
            return HttpResponse('PDF generation error!', status=500)

        pdf_data = buffer.getvalue()
        buffer.close()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cover_letter.name}.pdf"'
        response.write(pdf_data)

        return response


class CreateCoverLetterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CoverLetterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cover_letter_id = serializer.create(request.data)
            response = HttpResponse()
            response['id'] = cover_letter_id
            return response

        else:
            return HttpResponse("Data Not Valid")


class GetCoverLettersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        cover_letters = CoverLetter.objects.filter(user_id=id).all()
        serialized_cover_letters = serialize('json', cover_letters)
        response_json = json.loads(serialized_cover_letters)

        return JsonResponse(response_json, safe=False)