from django.urls import path

from src.apps.invitation_cards.views import InvitationCardCreateView , InvitationCardTemplateView

app_name = 'invitation_cards'
urlpatterns = [
    path('invition_card_create', InvitationCardCreateView.as_view(), name='invitation_card_create'),
    path('invitation_cards/<str:id>', InvitationCardTemplateView.as_view(),name='invitation_cards')
]

