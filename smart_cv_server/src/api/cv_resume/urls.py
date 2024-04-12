from django.urls import path, include
from rest_framework import routers

from .views import ResumeView

app_name = 'cv_resume'

router = routers.DefaultRouter()
router.register(r'', ResumeView)

urlpatterns = [
    path('', include(router.urls))
]
