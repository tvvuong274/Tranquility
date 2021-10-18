from django.urls import path
from api.v2.data_source_api.views import DataSourceApiView

urlpatterns = [
    path("", DataSourceApiView.as_view({"get": "list_all_data_source_api"}),
         name="data_source_api_list"),
    path(
        "templates/<int:template_id>/",
        DataSourceApiView.as_view({"get": "list_data_source_api_template"}),
        name="data_source_api_list_of_template"),
    path(
        "<int:data_source_api_id>/",
        DataSourceApiView.as_view({"get": "detail_data_source_api"}),
        name="data_source_api_detail", ),
    path("<int:data_source_api_id>/assign/", DataSourceApiView.as_view({"post": "copy"}),
         name="data_source_api_copy"),
]
