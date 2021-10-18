from django.urls import path, include
from api.v2.metadata.views import MetadataView, MetadataGroupView

urlpatterns = [
    path("groups/", MetadataGroupView.as_view({"get": "list_group"})),
    path("exist/", MetadataView.as_view({"get": "check_exist"})),
    path("", MetadataView.as_view({"get": "list", "post": "create"})),
    path("<int:metadata_id>/", MetadataView.as_view({"get": "detail_metadata", "put": "update", "delete": "delete"})),
    path("<int:metadata_id>/comments/", include('api.v2.metadata.comment.urls')),
]
