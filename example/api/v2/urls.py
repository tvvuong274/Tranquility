from django.urls import path, include

urlpatterns = [
    path('users/', include('api.v2.user.urls')),
    path('input_types/', include('api.v2.input_type.urls')),
    path('organization/', include('api.v2.organization.urls')),
    path('metadata/', include('api.v2.metadata.urls')),
    path('template_groups/', include('api.v2.template_group.urls')),
    path('templates/', include('api.v2.template.urls')),
    path('data_source_apis/', include('api.v2.data_source_api.urls')),
    # path('third_party_authorizations/', include('api.v2.authorization.urls')),
]
