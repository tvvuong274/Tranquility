from django.urls import path
from .views import MetadataCommentView

urlpatterns = [
    path("", MetadataCommentView.as_view({"post": "create", "get": "list"})),
    # path("<int:metadata_comment_id>/", MetadataCommentView.as_view({"patch": "update"})),
]