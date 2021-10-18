from django.urls import path, include

from api.v2.template_group.views import TemplateGroupView

urlpatterns = [
    path('', TemplateGroupView.as_view({'post': 'create', 'get': 'list'}), name="template_group_create_list"),
    path('exist/', TemplateGroupView.as_view({'get': 'check_exist'})),
    path('menu/', TemplateGroupView.as_view({'get': 'list_menu'}), name="template_group_list_menu"),
    path('<int:template_group_id>/', TemplateGroupView.as_view(
        {'get': 'detail_template_group', 'put': 'update', 'delete': 'delete'}), name="template_group_detail_update_delete"),

    path('<int:template_group_id>/folders/',
         include('api.v2.template_group.template_folder.urls')),
]
