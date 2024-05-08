from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from src.apps.cover_letter.models import CoverLetter


class TemplateViewCoverLetter(TemplateView):
    template_name = 'cover_letter.html'

    def get_context_data(self, **kwargs):
        _id = kwargs.get('id')
        cover_letter = get_object_or_404(CoverLetter, pk=_id)

        context = super(TemplateViewCoverLetter, self).get_context_data(
            cover_letter=cover_letter
        )
        return context


