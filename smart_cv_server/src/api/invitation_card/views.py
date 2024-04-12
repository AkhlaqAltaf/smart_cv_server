from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from src.api.invitation_card.serializers import InvitationSerializer
from src.apps.invitation_card.models import Invitation


class InvitationCardView(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class =InvitationSerializer
    permission_classes = [AllowAny]
