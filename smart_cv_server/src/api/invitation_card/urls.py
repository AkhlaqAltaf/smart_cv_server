from django.urls import include, path
from rest_framework import routers

from src.api.invitation_card.views import InvitationCardView, DownloadInvitationCardView

router = routers.DefaultRouter()
router.register(r'', InvitationCardView)
app_name = 'invitation_card'
urlpatterns = [
    path('', include(router.urls)),
    path('dowload/<int:invitation_id>', DownloadInvitationCardView.as_view(), name='download')
]