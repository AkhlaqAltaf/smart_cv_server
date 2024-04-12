from django.urls import path, include
from rest_framework import routers

from .views import ResumeCreateView

app_name = 'cv_resume'

router = routers.DefaultRouter()
router.register(r'', ResumeCreateView)

urlpatterns = [
    path('', include(router.urls))
]
