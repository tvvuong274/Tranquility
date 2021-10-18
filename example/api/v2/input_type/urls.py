from django.urls import path

from api.v2.input_type.views import InputTypeView

urlpatterns = [
    path("", InputTypeView.as_view({"get": "list"}), name="input_type_list"),
    path("<int:input_type_id>/formats/", InputTypeView.as_view({"get": "list_format"}), name="input_type_list_format"),
    path("<int:input_type_id>/formats/<int:input_type_format_id>/conditions/", InputTypeView.as_view({"get": "json_condition"}),
        name="input_type_json_condition"),
]
