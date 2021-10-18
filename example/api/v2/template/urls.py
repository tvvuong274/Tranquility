from django.urls import path, include
from api.v2.template.views import TemplateView


urlpatterns = [
    path('', TemplateView.as_view({'get': 'list'})),
    path('exist/', TemplateView.as_view({'get': 'check_exist'})),
    path('<int:template_id>/versions/', include('api.v2.template.version.urls')),
    path('<int:template_id>/eforms/', include('api.v2.template.eform.urls')),

]
