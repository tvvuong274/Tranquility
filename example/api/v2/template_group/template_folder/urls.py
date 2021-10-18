from django.urls import path, include
from api.v2.template_group.template_folder.views import FolderViews

urlpatterns = [
    path("", FolderViews.as_view({"post": "create", "get": "list"})),
    path("exist/", FolderViews.as_view({"get": "check_exist"})),
    path("<int:folder_id>/", FolderViews.as_view({"put": "update", "delete": "delete"})),
    path("menu/", FolderViews.as_view({"get": "list_menu"})),
]
