from django.urls import path, include
from api.v2.template.version.views import VersionView

urlpatterns = [
    path("", VersionView.as_view({"get": "list_version"})),
]
