from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from smart_cv_server import settings
from src.api.cover_letter.views import CoverLetterView, DownloadCoverLetter, CreateCoverLetterView

app_name = 'cover_letter'
router = routers.DefaultRouter()
router.register(r'', CoverLetterView)

urlpatterns = [
                  path('', include(router.urls)),
                  path('download/<int:cover_letter_id>', DownloadCoverLetter.as_view(), name='download'),
                  path('create', CreateCoverLetterView.as_view(), name='create'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
