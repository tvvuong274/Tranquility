from django.conf.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from idm_config.root_local import SWAGGER_SUB_ENDPOINT, REDOC_SUB_ENDPOINT

urlpatterns = [
    # path('v1/', include('api.v1.urls')),
    path('v2/', include('api.v2.urls')),
]

# API DOCUMENT URLS
# --------------------------------------------------------------------------------------------------
# Urls listed in api_url_patterns will appear on schema.
api_url_v1_patterns = [
    # path('api/v1/', include("api.v1.urls")),
]

api_url_v2_patterns = [
    path('api/v2/', include("api.v2.urls")),
]

urlpatterns += [
    path('v1/schema/', SpectacularAPIView.as_view(urlconf=api_url_v1_patterns, api_version='v1'), name="schema_v1"),
    path('v1/' + SWAGGER_SUB_ENDPOINT, SpectacularSwaggerView.as_view(url_name="schema_v1"), name='swagger_v1'),
    path('v1/' + REDOC_SUB_ENDPOINT, SpectacularRedocView.as_view(url_name="schema_v1"), name='redoc_v1'),

    path('v2/schema/', SpectacularAPIView.as_view(urlconf=api_url_v2_patterns, api_version='v2'), name="schema_v2"),
    path('v2/' + SWAGGER_SUB_ENDPOINT, SpectacularSwaggerView.as_view(url_name="schema_v2"), name='swagger_v2'),
    path('v2/' + REDOC_SUB_ENDPOINT, SpectacularRedocView.as_view(url_name="schema_v2"), name='redoc_v2')
]
