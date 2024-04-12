from django.urls import include, path
from .docs import get_swagger_doc_schema_view

app_name = 'api'
urlpatterns = []

""" TO LEARN SWAGGER - https://drf-yasg.readthedocs.io/en/stable/readme.html --------------------------------------- """


schema_view = get_swagger_doc_schema_view()
urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

""" MAIN URLS ------------------------------------------------------------------------------------------------------ """

""" Version 1 of the API ------------------------------------------------------------------------------------------- """
urlpatterns += [
    path('auth/', include('src.api.auth.urls', namespace='auth')),
    path('cv_resume/' , include('src.api.cv_resume.urls', namespace='cv_resume/')),
    path('users/', include('src.api.users.urls', namespace='users')),

]
